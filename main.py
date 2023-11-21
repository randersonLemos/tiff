import rasterio
from rasterio.plot import show
import matplotlib
import pandas
matplotlib.use('TkAgg')

with rasterio.open('./MAPBIOMAS-EXPORT/mapbiomas-brazil-collection-80-campinas-2022.tif') as image:
    mat = image.read()

import IPython; IPython.embed()


