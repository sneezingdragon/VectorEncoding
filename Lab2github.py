import glob
import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon, MultiPoint, MultiPolygon
from rasterstats import zonal_stats
dictionary = {'dist':[], 'num_coords':[], 'poly':[]}
files=glob.glob(r'C:\Users\sneez\OneDrive\Documents\lab2_data\data\districts\*.txt')
for items in files: 
    x = pd.read_csv(items, delim_whitespace=True)
    coords = list(zip(x['X'],x['Y']))
    poly = Polygon(coords)
    dictionary['dist'].append(items[-6:-4])
    dictionary['num_coords'].append(len(coords))
    dictionary['poly'].append(poly)
    dataframe = pd.DataFrame(dictionary)
gdf = gpd.GeoDataFrame(dataframe, geometry = 'poly')
gdf = gdf.set_crs('epsg:4326')
gdf.to_file('districts.shp')
Farmland = {'Dist':['01','05','06','01','05','06'], 'year':['2004','2004','2004','2009','2009','2009'], 'per_cover':[]}
Agr_list = glob.glob(r'C:\Users\sneez\OneDrive\Documents\lab2_data\data\agriculture\*.tif'                                              
for layers in Agr_list:
    stats = pd.DataFrame(zonal_stats('districts.shp', layers, stats = ['count', 'sum']))
    count = list(stats['count'])
    sumbitch = list(stats['sum'])
    cropland = ([i / j for i, j in zip(sumbitch, count)])
    for percentage in cropland:
        Farmland['per_cover'].append(percentage)  
FinalFarmland=pd.DataFrame(Farmland)
FinalFarmland