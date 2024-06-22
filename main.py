from openmeteopy import OpenMeteo
from openmeteopy.daily import DailyHistorical
from openmeteopy.hourly import HourlyHistorical
from openmeteopy.options import HistoricalOptions

# Latitude, Longitude
longitude = 33.89
latitude = -6.31

hourly = HourlyHistorical()
daily = DailyHistorical()
options = HistoricalOptions(
    latitude, longitude, start_date="2022-12-31", end_date="2023-02-26"
)

mgr = OpenMeteo(options, hourly.all(), daily.all())

# Download data
meteo = mgr.get_pandas()
print(meteo)
