import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import contextily as ctx

data = [df["STATION"], df["LATITUDE"], df["LONGITUDE"]]
headers = ["STATION","LAT", "LONG"]
df3 = pd.concat(data, axis=1, keys=headers)

df3 = df3.fillna('')\
      .groupby(df3.columns.tolist()).apply(len)\
      .rename('COUNT')\
      .reset_index()\
      .replace('',np.nan)

plt.scatter(df3['LONG'], df3['LAT'], c=df3['COUNT'])
plt.colorbar()
plt.show()

geometry = geopandas.points_from_xy(df3.LONG, df3.LAT)

gdf = geopandas.GeoDataFrame(
    df3, 
    crs='EPSG:4326',
    geometry=geometry)

gdf['values'] = df3['COUNT']
gdf = gdf.to_crs(epsg=3857)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world.to_crs(epsg=3857)

# Restringir a tailandia
ax = world[world.name == 'Thailand'].plot(
    figsize=(15, 15),
    color='white',
    alpha=0.5,
    edgecolor='k')

ctx.add_basemap(ax)

# Plot geodataframe
gdf.plot(ax=ax, column='values', cmap='plasma', legend=True, markersize=(gdf['values']/20))
plt.savefig('thailand_stations.jpg')
plt.show()