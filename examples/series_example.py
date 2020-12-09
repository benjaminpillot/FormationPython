import pandas as pd

from matplotlib import pyplot as plt

fig, ax = plt.subplots()
ax.set_ylabel("temperature")
ax.set_title("one-year temperature time series")

# Read some temperature time series
# 'squeeze' option allows returning a series when there is only one column
temperature = pd.read_csv("examples/timeseries.csv", index_col=0, parse_dates=True, date_parser=pd.DatetimeIndex, header=None, squeeze=True)

# Plot hourly time series
temperature.plot(ax=ax, label="hourly")

# Use the resample function to aggregate and average values per day, and plot daily mean temperature
daily_temperature = temperature.resample('D').mean()
daily_temperature.plot(ax=ax, label="daily")

ax.legend()
plt.show()