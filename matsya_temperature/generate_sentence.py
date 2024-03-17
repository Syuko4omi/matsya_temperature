import random
from get_temperature_and_month import get_temperature_and_month
from matsya_class import Matsya
from text_process_funcs import process_tokens
from specific_token_generator import this_is_gen, decorator_gen, desune_gen
import config


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
        return random.choice(config.error_phrase)

    matsya = Matsya(temperature, month)
    random_value = random.random()

    if random_value < 0.8:
        return generate_sentence_climate(matsya.climate)
    elif random_value < 0.99:
        return generate_sentence_season(matsya.season)
    else:
        return random.choice(config.template_phrase)


def generate_sentence_climate(climate: str) -> str:
    prefix = this_is_gen("climate") + decorator_gen()
    climate_phrase = [random.choice(config.climate_phrase[climate])]
    postfix = desune_gen("climate")

    return "".join(process_tokens(prefix + climate_phrase + postfix))


def generate_sentence_season(season: str) -> str:
    prefix = this_is_gen("season") + decorator_gen()
    season_phrase = [random.choice(config.season_phrase[season])]
    postfix = desune_gen("season")

    return "".join(process_tokens(prefix + season_phrase + postfix))
