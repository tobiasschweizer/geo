from typing import NamedTuple


class GPS(NamedTuple):
    degrees: int
    minutes: int
    seconds: float


class LV95(NamedTuple):
    longitude: float
    latitude: float


def gps_to_sexagesimal_seconds(gps: GPS) -> float:
    """
    Given a GPS coordinate as degrees, minutes, seconds,
    returns the coordinate as sexagesimal seconds.
    @param gps:
    @return:
    """
    return gps.degrees * 3600 + gps.minutes * 60 + gps.seconds


def convert_wgs84_to_lv95(longitude_d: float, latitude_d: float) -> LV95:
    """
    Converts GPS coordinates to Swiss coordinates (LV95).

    https://www.swisstopo.admin.ch/de/karten-daten-online/calculation-services.html
    https://www.swisstopo.admin.ch/content/swisstopo-internet/de/online/calculation-services/_jcr_content/contentPar/tabs/items/dokumente_und_publik/tabPar/downloadlist/downloadItems/7_1467103072612.download/ch1903wgs84_d.pdf

    @param longitude_d: Longitude in sexagesimal seconds.
    @param latitude_d: Latitude in sexagesimal seconds.
    @return: Coordinates in the Swiss system LV95.
    """

    e = 2600072.37 + 211455.93 * longitude_d - 10938.51 * longitude_d * latitude_d - 0.36 * longitude_d * pow(latitude_d, 2) - 44.54 * pow(
        longitude_d, 3)

    n = 1200147.07 + 308807.95 * latitude_d + 3745.25 * pow(longitude_d, 2) + 76.63 * pow(latitude_d, 2) - 194.56 * pow(longitude_d,
                                                                                                                        2) * latitude_d + 119.79 * pow(
        latitude_d, 3)

    return LV95(e, n)


longitude = GPS(8, 43, 49.79)
longitude_sexa: float = gps_to_sexagesimal_seconds(longitude)
longitude_d: float = (longitude_sexa - 26782.5) / 10000

latitude = GPS(46, 2, 38.87)
latitude_sexa: float = gps_to_sexagesimal_seconds(latitude)
latitude_d: float = (latitude_sexa - 169028.66) / 10000

print(convert_wgs84_to_lv95(longitude_d=longitude_d, latitude_d=latitude_d))


