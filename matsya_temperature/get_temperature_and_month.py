import os

from pyowm.owm import OWM
from pyowm.utils import formatting
from pyowm.utils.config import get_default_config


def get_temperature_and_month(
    location: str = "Tokyo, JP",
) -> tuple[float, int]:
    """
    Args:
        location (str): place we want to know its weather

    Returns:
        apparent temperature (float): temperature we can feel
        month (int)

    Examples:
        >>> get_apparent_temperature_and_month("Tokyo, JP")
        19.44 3

    Note:
        if there is an error this function always returns (-1000.0, 100)

    """

    config_dict = get_default_config()
    owm = OWM(os.environ["OWM_API_KEY"], config_dict)

    try:
        mgr = owm.weather_manager()
        w = mgr.weather_at_place(location).weather
        temperature = w.temperature(
            "celsius"
        )  # e.g., {'temp': 20.32, 'temp_max': 22.58, 'temp_min': 18.75, 'feels_like': 19.69, 'temp_kf': None}
        date = formatting.timeformat(
            w.ref_time, "date"
        )  # datetime.datetime object  e.g., "2024-03-17 05:40:10+00:00"

        return temperature["feels_like"], date.month
    except Exception:
        return -1000.0, 100
