from openmeteopy import OpenMeteo
from openmeteopy.daily import DailyHistorical
from openmeteopy.hourly import HourlyHistorical
from openmeteopy.options import HistoricalOptions

# Latitude, Longitude
longitude = 51.4475302
latitude = 35.737952

hourly = HourlyHistorical()
daily = DailyHistorical()
options = HistoricalOptions(
    latitude, longitude, start_date="2022-12-31", end_date="2023-02-26"
)

mgr = OpenMeteo(options, hourly.all(), daily.all())

# Download data
meteo = mgr.get_pandas()
print(meteo)
