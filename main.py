import datetime
import logging
import pathlib

import geopandas as gpd
from openmeteopy import OpenMeteo
from openmeteopy.hourly import HourlyHistorical
from openmeteopy.options import HistoricalOptions

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    districts: gpd.GeoDataFrame = gpd.read_file("districts.geojson")

    since = datetime.date(2024, 4, 28)
    to = datetime.date(2024, 5, 18)

    for _, district in districts.iterrows():
        logger.info("Reading weather data for %s", district.name)

        if pathlib.Path(f"{district.id}.csv").exists:
            logger.info("Weather data for %d is already downloaded", district.name)
            continue

        center = district.geometry.centroid

        longitude = center.x
        latitude = center.y

        # Data is available for at least 2 days ago.
        hourly = HourlyHistorical()
        options = HistoricalOptions(
            latitude,
            longitude,
            start_date=since,
            end_date=to,
        )

        mgr = OpenMeteo(options, hourly.all(), None)

        mgr.get_pandas().to_csv(f"{district.id}.csv")
