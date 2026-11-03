'''tic_toc
Demonstrate tic toc profiling.
'''
import time

import xarray as xr
from icecream import ic
from scipy import stats
import numpy as np

#  Import data
tic = time.time()
ds = xr.load_dataset('/Users/danielhueholt/Data/ev228_data/gridded/era5_t2m_1997-2025.nc')
toc = time.time() - tic
ic('Time elapsed: ', toc)
ic(ds)