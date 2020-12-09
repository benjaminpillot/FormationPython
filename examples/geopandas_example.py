import geopandas
from matplotlib import pyplot as plt
import numpy as np

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))

print(world.head())

# Basic plot, random colors
world.plot()


# Plot by GDP per capta
# world = world[(world.pop_est>0) & (world.name!="Antarctica")]
# world['gdp_per_cap'] = world.gdp_md_est / world.pop_est
# world.plot(column='gdp_per_cap')

# Plot population estimates with an accurate legend
# fig, ax = plt.subplots(1, 1)
# world.plot(column='pop_est', ax=ax, legend=True)

# Use quantiles
# world.plot(column='gdp_per_cap', cmap='OrRd', scheme='quantiles');

# See missing data
# world.loc[np.random.choice(world.index, 40), 'pop_est'] = np.nan
# world.plot(column='pop_est', legend=True, missing_kwds={'color': 'lightgrey'});



# Look at capitals

# Check crs
# cities = cities.to_crs(world.crs)

# Plot cities over world
# ax = cities.plot(color='k', zorder=2)
# world.plot(ax=ax, zorder=1);


plt.show()