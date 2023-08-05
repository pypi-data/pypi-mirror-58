#-------------------------------------------------------------------------------
#
# Handles the WPS requests to the VirES server
#
# Authors: Ashley Smith <ashley.smith@ed.ac.uk>
#          Martin Paces <martin.paces@eox.at>
#
#-------------------------------------------------------------------------------
# Copyright (C) 2018 EOX IT Services GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies of this Software or works derived from this Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#-------------------------------------------------------------------------------


import os
try:
    from io import BytesIO
except ImportError:
    # Python 2 backward compatibility
    import StringIO as BytesIO
import tempfile
import shutil
if os.name == "nt":
    import atexit

import numpy
import pandas
import xarray
import cdflib

from ._wps import time_util

CDF_EPOCH_1970 = 62167219200000.0

# Dimension names for data columns with extra dimensions
#  and suffixes to use in expanded dataframes
COLUMN_INFO = {
    # MAG datasets
    # NEC mapping to also apply to any column name containing "B_NEC"
    "B_NEC":      ("NEC", ["_N", "_E", "_C"]),
    # VFM frame
    "B_VFM":      ("VFM", ["_i", "_j", "_k"]),
    "dB_Sun":     ("VFM", ["_i", "_j", "_k"]),
    "dB_AOCS":    ("VFM", ["_i", "_j", "_k"]),
    "dB_other":   ("VFM", ["_i", "_j", "_k"]),
    "B_error":    ("VFM", ["_i", "_j", "_k"]),
    # quartenions
    "q_NEC_CRF":  ("", ["_1", "_i", "_j", "_k"]),

    # TEC datasets
    # WGS84 frame
    "GPS_Position": ["_X", "_Y", "_Z"],
    "LEO_Position": ["_X", "_Y", "_Z"],

    # auxiliaries
#     "SunVector":
#     "DipoleAxisVector":
    # Cases with more than 1 dim not supported
#     "QDBasis":
}


def make_pandas_DataFrame_from_csv(csv_filename):
    """Load a csv file into a pandas.DataFrame

    Set the Timestamp as a datetime index.

    Args:
        csv_filename (str)

    Returns:
        pandas.DataFrame

    """
    try:
        # df = pandas.read_csv(BytesIO(self._data))
        df = pandas.read_csv(csv_filename)
    except Exception:
        raise Exception("Bad or empty csv.")
    # Convert to datetime objects
    df['Timestamp'] = df['Timestamp'].apply(
        time_util.parse_datetime
        )
    # Convert the columns of vectors from strings to lists
    # Returns empty dataframe when retrieval from server is empty
    if len(df) != 0:
        # Convert the columns of vectors from strings to lists
        for col in df:
            if type(df[col][0]) is str:
                if df[col][0][0] == '{':
                    df[col] = df[col].apply(
                        lambda x: [
                            float(y) for y in x.strip('{}').split(';')
                        ])
    df.set_index('Timestamp', inplace=True)
    return df


def make_pandas_DataFrame_from_cdf(cdf_filename, expand=False):
    """Load a csv file into a pandas.DataFrame

    Args:
        cdf_filename (str)
        expand (bool)

    Returns:
        pandas.DataFrame

    """

    # Open the cdf and identify column names
    try:
        cdf = cdflib.CDF(cdf_filename)
        # Get column names except for Timestamp
        cols = cdf.cdf_info()['zVariables']
        cols = [c for c in cols if c!="Timestamp"]
    except Exception:
        cdf.close()
        raise Exception("Error reading CDF")

    # Identify columns which will be expanded into multiple columns
    if expand:
        cols_to_expand = [c for c in cols
                            if c in COLUMN_INFO.keys()
                            or "B_NEC" in c]
    else:
        cols_to_expand = []

    try:
        # Initialise dataframe with Timestamp as index
        df = pandas.DataFrame(index=cdf.varget("Timestamp"))
    except ValueError:
        # Handle case where retrieval from server is empty
        #  Returns empty dataframe with correct column names
        #  so merging df's will work okay
        df = pandas.DataFrame(columns=["Timestamp"])
        for col in cols:
            if col in cols_to_expand:
                if "B_NEC" in col:
                    col_base_name = "B_NEC"
                else:
                    col_base_name = col
                for component, suffix in enumerate(
                        COLUMN_INFO[col_base_name][1]):
                    df[col + suffix] = None
            else:
                df[col] = None
        df = df.set_index("Timestamp")
    else:
        # Handle the usual case where there is data present
        # Add the other (non-Timestamp) columns to the dataframe
        for col in cols:
            if col in cols_to_expand:
                if "B_NEC" in col:
                    col_base_name = "B_NEC"
                else:
                    col_base_name = col
                for component, suffix in enumerate(
                        COLUMN_INFO[col_base_name][1]):
                    df[col + suffix] = cdf.varget(col)[:, component]
            else:
                df[col] = list(cdf.varget(col))
        # Convert timestamps to datetime objects
        df.index = pandas.to_datetime(
            (df.index - CDF_EPOCH_1970)/1e3,
            unit='s'
        )
    finally:
        cdf.close()

    return df


def make_xarray_Dataset_from_cdf(cdf_filename):
    """Load a cdf file as an xarray Dataset

    Use cdflib to read the cdf file. Create an xarray.Dataset with the
    Timestamp as the coords (as datetime.datetime).
    3-D vectors have dimension label 'dim'. Other cases not yet handled.

    Args:
        cdf_filename (str)

    Returns:
        xarray.Dataset

    """
    cdf = cdflib.CDF(cdf_filename)
    # Load time and convert to Unix time
    try:
        time = cdf.varget("Timestamp")
    except ValueError:
        cdf.close()
        return None
    # Return None when the CDF is empty
    if time is None:
        return None
    time = (time-CDF_EPOCH_1970)/1e3
    # Now convert to a DatetimeIndex
    time = pandas.to_datetime(time, unit='s')
    # Initialise the Dataset with the Timestamp index
    ds = xarray.Dataset(coords={"Timestamp": time})
    # Loop through each variable available in the CDF and append them to the
    #   Dataset, attaching the Timestamp index to each. Attach dimension names
    #   based on the name of the variable. B_NEC variables get the NEC dim name
    keys = [k for k in cdf.cdf_info()["zVariables"] if k != "Timestamp"]
    for k in keys:
        if cdf.varinq(k)["Num_Dims"] == 0:
            # 1D (scalar series) data
            ds[k] = (("Timestamp",), cdf.varget(k))
        # 2D (vector series) case
        elif cdf.varinq(k)["Num_Dims"] == 1:
            if "B_NEC" in k:
                dimname = "NEC"
            else:
                dimname = "%s_dim1" % k
            ds[k] = (("Timestamp", dimname), cdf.varget(k))
        # 3D case (matrix series), e.g. QDBasis
        elif cdf.varinq(k)["Num_Dims"] == 2:
            ds[k] = (("Timestamp", "%s_dim1" % k, "%s_dim2" % k), cdf.varget(k))
        else:
            raise NotImplementedError("{}: array too complicated".format(k))
    cdf.close()
    return ds


class ReturnedDataFile(object):
    """For handling individual files returned from the server.

    Holds the data returned from the server and the data type.
    Data is held in a NamedTemporaryFile, which is automatically closed and
    destroyed when it goes out of scope.
    Provides output to different file types and data objects.

    """

    def __init__(self, filetype=None, tmpdir=None):
        self._supported_filetypes = ("csv", "cdf", "nc")
        self.filetype = str() if filetype is None else filetype
        if tmpdir is not None:
            if not os.path.exists(tmpdir):
                raise Exception("tmpdir does not exist")
        if os.name == "nt":
            self._file = tempfile.NamedTemporaryFile(
                prefix="vires_", dir=tmpdir, delete=False)
            self._file.close()
            atexit.register(os.remove, self._file.name)
        else:
            self._file = tempfile.NamedTemporaryFile(
                prefix="vires_", dir=tmpdir)


    def __str__(self):
        return "viresclient ReturnedDataFile object of type " + self.filetype + \
            "\nSave it to a file with .to_file('filename')" + \
            "\nLoad it as a pandas dataframe with .as_dataframe()" + \
            "\nLoad it as an xarray dataset with .as_xarray()"

    def open_cdf(self):
        """Returns the opened file as cdflib.CDF
        """
        return cdflib.CDF(self._file.name)

    def _write_new_data(self, data):
        """Replace the tempfile contents with 'data' (bytes)

        """
        if not isinstance(data, bytes):
            raise TypeError("data must be of type bytes")
        # If on Windows, the file will be closed so needs to be re-opened:
        with open(self._file.name, "wb") as temp_file:
            temp_file.write(data)

    def _write_file(self, filename):
        """Write the tempfile out to a regular file

        """
        with open(self._file.name, "rb") as temp_file:
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(temp_file, out_file)

    @property
    def filetype(self):
        """Filetype is one of ("csv", "cdf", "nc")
        """
        return self._filetype

    @filetype.setter
    def filetype(self, value):
        if not isinstance(value, str):
            raise TypeError("filetype must be a string")
        value = value.lower()
        if value not in self._supported_filetypes:
            raise TypeError("Chosen filetype must be one of: {}".format(
                            self._supported_filetypes
                            ))
        self._filetype = value

    @staticmethod
    def _check_outfile(path, path_extension, overwrite=False):
        """Check validity of path and extension, and if it exists already

        """
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        if path.split('.')[-1].lower() != path_extension:
            raise TypeError("Filename extension should be {}".format(
                path_extension
                ))
        if os.path.isfile(path) and not overwrite:
            raise Exception(
                "File not written as it already exists and overwrite=False"
                )

    def to_file(self, path, overwrite=False):
        """Saves the data to the specified file.

        Only write to file if it does not yet exist, or if overwrite=True.
        Currently handles CSV and CDF formats.

        Args:
            path (str): path to the file to save as
            overwrite (bool): Will overwrite existing file if True

        """
        self._check_outfile(path, self.filetype, overwrite)
        self._write_file(path)
        print("Data written to", path)

    def to_netcdf(self, path, overwrite=False):
        """Saves the data as a netCDF4 file (this is compatible with HDF5)

        Extension should be .nc

        """
        self._check_outfile(path, 'nc', overwrite)
        # Convert to xarray Dataset
        ds = self.as_xarray()
        ds.to_netcdf(path)
        print("Data written to", path)

    def as_dataframe(self, expand=False):
        """Convert the data to a pandas DataFrame.

        Returns:
            pandas.DataFrame

        """
        if self.filetype == 'csv':
            if expand:
                raise NotImplementedError
            df = make_pandas_DataFrame_from_csv(self._file.name)
        elif self.filetype == 'cdf':
            df = make_pandas_DataFrame_from_cdf(self._file.name, expand=expand)
        return df

    def as_xarray(self, group=None):
        """Convert the data to an xarray Dataset.

        Note:
            Does not support csv

            Only supports scalar and 3D vectors (currently)

        Returns:
            xarray.Dataset

        """
        if self.filetype == 'csv':
            raise NotImplementedError("csv to xarray is not supported")
        elif self.filetype == 'cdf':
            ds = make_xarray_Dataset_from_cdf(self._file.name)
        elif self.filetype == 'nc':
            ds = xarray.open_dataset(self._file.name, group=group)
        return ds


class ReturnedData(object):
    """Flexible object for working with data returned from the server

    Holds a list of ReturnedDataFile objects.
    The number of them, N, is set upon initialisation.
    Access the ReturnedDataFile objects directly via the list in ReturnedData.contents.

    Example usage::

        ...
        data = request.get_between(..., ...)
        data.as_xarray()
        data.as_dataframe(expand=True)
        data.to_file()

    """

    def __init__(self, filetype=None, N=1, tmpdir=None):
        self.contents = [
            ReturnedDataFile(filetype=filetype, tmpdir=tmpdir) for i in range(N)
            ]
        # filetype checking / conversion has been done in ReturnedDataFile
        self.filetype = self.contents[0].filetype

    def __str__(self):
        return "viresclient ReturnedData object of type "+self.filetype +\
            "\nSave it to a file with .to_file('filename')" + \
            "\nLoad it as a pandas dataframe with .as_dataframe()" + \
            "\nLoad it as an xarray dataset with .as_xarray()"

    @property
    def filetype(self):
        """Filetype string
        """
        return self._filetype

    @filetype.setter
    def filetype(self, value):
        if not isinstance(value, str):
            raise TypeError("filetype must be a string")
        self._filetype = value

    @property
    def sources(self):
        """ Get list of source product identifiers.
        """
        # .globalattsget().get(...) returns either a string of one variable
        #  or a list of strings. The lambda function converts these to a list.
        # Unique values from each file are collected within a set.
        sources = set()
        for item in self._contents:
            sources.update(
                (lambda x: [x] if type(x) is str else x)
                (item.open_cdf().globalattsget().get('ORIGINAL_PRODUCT_NAMES', [])),
            )
        return sorted(sources)

    @property
    def magnetic_models(self):
        """ Get list of magnetic models used.
        """
        models = set()
        for item in self._contents:
            models.update(
                (lambda x: [x] if type(x) is str else x)
                (item.open_cdf().globalattsget().get('MAGNETIC_MODELS', [])),
            )
        return sorted(models)

    @property
    def range_filters(self):
        """ Get list of filters applied.
        """
        filters = set()
        for item in self._contents:
            filters.update(
                (lambda x: [x] if type(x) is str else x)
                (item.open_cdf().globalattsget().get('DATA_FILTERS', [])),
            )
        return sorted(filters)

    @property
    def contents(self):
        """List of ReturnedDataFile objects
        """
        return self._contents

    @contents.setter
    def contents(self, value):
        if not isinstance(value, list):
            raise TypeError("ReturnedData.contents should be a list")
        for i in value:
            if not isinstance(i, ReturnedDataFile):
                raise TypeError(
                    "Items in ReturnedData.contents should be"
                    "of type ReturnedDataFile")
        self._contents = value

    def as_dataframe(self, expand=False):
        """Convert the data to a pandas DataFrame.

        If expand is True, expand some columns, e.g.:

        B_NEC -> B_NEC_N, B_NEC_E, B_NEC_C

        B_VFM -> B_VFM_i, B_VFM_j, B_VFM_k

        Args:
            expand (bool)

        Returns:
            pandas.DataFrame

        """
        return pandas.concat(
            [d.as_dataframe(expand=expand) for d in self.contents])

    def as_xarray(self):
        """Convert the data to an xarray Dataset.

        Returns:
            xarray.Dataset

        """
        # ds_list is a list of xarray.Dataset objects
        #  - they are created from each file in self.contents
        # Some of them may be empty because of the time window they cover
        #  and the filtering that has been applied.
        ds_list = []
        for i, data in enumerate(self.contents):
            ds_part = data.as_xarray()
            if ds_part is None:
                print("Warning: ",
                      "Unable to create dataset from part {} of {}".format(
                        i+1, len(self.contents)),
                      "\n(This part is likely empty)")
            else:
                # Collect the non-empty Datasets
                ds_list.append(ds_part)
        if len(ds_list) == 1:
            ds = ds_list[0]
        else:
            ds_list = [i for i in ds_list if i is not None]
            if ds_list == []:
                return None
            ds = xarray.concat(ds_list, dim="Timestamp")
        # # Test this other option:
        # ds = self.contents[0].as_xarray()
        # for d in self.contents[1:]:
        #     ds = xarray.concat([ds, d.as_xarray()], dim="Timestamp")
        # return ds
        #
        # https://github.com/pydata/xarray/issues/1379
        # concat is slow. Maybe try extracting numpy arrays and rebuilding ds

        # Set the original data sources and models used as metadata
        ds.attrs["Sources"] = self.sources
        ds.attrs["MagneticModels"] = self.magnetic_models
        ds.attrs["RangeFilters"] = self.range_filters
        return ds

    def to_files(self, paths, overwrite=False):
        """Saves the data to the specified files.

        Only write to file if it does not yet exist, or if overwrite=True.
        Currently handles CSV and CDF formats.

        Args:
            paths (list of str): paths to the files to save as
            overwrite (bool): Will overwrite existing file if True

        """
        nfiles = len(self.contents)
        if not isinstance(paths, list) or not isinstance(paths[0], str):
            raise TypeError("paths must be a list of strings")
        if len(paths) != nfiles:
            raise Exception(
                "Number of paths must equal number of files ({})".format(
                    nfiles
                ))
        for path, retdata in zip(paths, self.contents):
            retdata.to_file(path, overwrite)

    def to_file(self, path, overwrite=False):
        """Saves the data to the specified file, when data is only in one file.

        Only write to file if it does not yet exist, or if overwrite=True.
        Currently handles CSV and CDF formats.

        Args:
            path (str): path to the file to save as
            overwrite (bool): Will overwrite existing file if True

        """
        if len(self.contents) != 1:
            raise Exception("Data is split into multiple files. "
                            "Use .to_files instead"
                            )
        self.contents[0].to_file(path, overwrite)
