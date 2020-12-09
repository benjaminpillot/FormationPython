# Python tools for the scientist
There is a lot of Python packages, like a lot. Here we will go through good Python distribution starters.

## Python packages for the scientist
* ``numpy``: a must-have. Especially useful for people coming from Matlab. Made for working with matrices and big arrays (such as rasters).
* ``scipy``: the other must-have, together with ``numpy``. Made especially for the scientist.
* ``pandas``: the other other must-have, very useful when working with datasets, tables and time series.
* ``matplotlib``: to make nice plots and graphs.

## Python packages for the GIS scientist/engineer
When working with GIScience, the following packages will make your life easier:
* ``geopandas``: for working with vectors and shapes
* ``rasterio`` and ``gdal``: for working with rasters
* ``networkx``: for working with networks and corresponding graphs (shortest path, etc.)
* ``rtree``: for spatial indexing (useful when requiring speed up for large vector datasets)
* ``folium``: for visualizing data that's been manipulated in Python on interactive leaflet maps (very useful together with Jupyter notebooks), see [here](https://python-visualization.github.io/folium/quickstart.html#Getting-Started)

## Other useful Python packages
* ``sqlalchemy``: for working with sql databases
* ``ipython``: a nice console for Python data scientists
* ``jupyter``: for jupyter notebooks (see below)

## Create a Conda distribution with useful packages
Conda presents the advantage of installing a whole distribution at once. Let's create a conda environment with some useful packages:
```shell
$ conda create -n my_awesome_env numpy scipy pandas matplotlib geopandas ipython jupyter
```

## Install a package on the fly
Whenever you need a new package, use `pip` in your virtual environment (either virtualenv or conda):
```shell
$ pip install folium
```

## Jupyter notebooks: mixing formatted text and code (see [here](https://mybinder.org/v2/git/https%3A%2F%2Fframagit.org%2Fbenjaminpillot%2Fcovid-19/master))

Whenever you want to present some code, you may use the Jupyter notebooks, a useful tool for data science presentation. It allows for mixing text (Markdown) and code in the same document.
It opens in a browser, and allows for directly coding inside. You may implement LaTeX formulas alongside Python code snippets.

