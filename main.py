import datetime

from openmeteopy import OpenMeteo
from openmeteopy.daily import DailyHistorical
from openmeteopy.options import HistoricalOptions

# Latitude, Longitude
longitude = 51.4475302
latitude = 35.737952

# Data is available for at least 2 days ago.
daily = DailyHistorical()
options = HistoricalOptions(
    latitude,
    longitude,
    start_date=datetime.date.today() - datetime.timedelta(days=2),
    end_date=datetime.date.today() - datetime.timedelta(days=2),
)

mgr = OpenMeteo(options, None, daily.all())

# Download data
meteo = mgr.get_pandas()
print(meteo)
