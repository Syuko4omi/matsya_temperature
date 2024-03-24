import random

from matsya_temperature.config import (
    climate_phrase,
    error_phrase,
    season_phrase,
    template_phrase,
)
from matsya_temperature.get_temperature_and_month import get_temperature_and_month
from matsya_temperature.matsya_class import Matsya
from matsya_temperature.specific_token_generator import (
    decorator_gen,
    desune_gen,
    this_is_gen,
)
from matsya_temperature.text_process_funcs import process_tokens


def generate_sentence() -> str:
    """
    Returns:
        sentence (str): matsya-like sentence

    Examples:
        >>> generate_sentence()
        さﾑ
    """
    temperature, month = get_temperature_and_month()
    if temperature == -1000.0:
        return random.choice(error_phrase)

    matsya = Matsya(temperature, month)
    random_value = random.random()

    if random_value < 0.8:
        return generate_sentence_climate(matsya.climate)
    elif random_value < 0.99:
        return generate_sentence_season(matsya.season)
    else:
        return random.choice(template_phrase)


def generate_sentence_climate(climate: str) -> str:
    prefix = this_is_gen("climate") + decorator_gen()
    climate_tokens = [random.choice(climate_phrase[climate])]
    postfix = desune_gen("climate")

    return "".join(process_tokens(prefix + climate_tokens + postfix))


def generate_sentence_season(season: str) -> str:
    prefix = this_is_gen("season") + decorator_gen()
    season_tokens = [random.choice(season_phrase[season])]
    postfix = desune_gen("season")

    return "".join(process_tokens(prefix + season_tokens + postfix))
