import random
import mojimoji
from get_temperature_and_month import get_temperature_and_month
from matsya_class import Matsya
import config


def generate_sentence():
    # temperature, month = get_temperature_and_month()
    temperature, month = -1.2, 1
    if temperature == -1000.0:
        return random.choice(config.error_phrase)

    matsya = Matsya(temperature, month)
    if random.random() < 0.78:
        return generate_sentence_climate(matsya.climate)
    elif random.random() < 0.98:
        return generate_sentence_season(matsya.season)
    else:
        return random.choice(config.template_phrase)


def process_tokens(tokens):
    step_1 = remove_empty_string_from_list(tokens)
    step_2 = add_exclamation_to_short_or_long_sentence(step_1)
    step_3 = convert_zenkaku_katakana_to_hankaku(step_2)
    step_4 = add_symbols(step_3)
    return step_4


def remove_empty_string_from_list(tokens):
    return list(filter(lambda x: x != "", tokens))


def add_exclamation_to_short_or_long_sentence(tokens):
    if len(tokens) == 1 and len(tokens[0]) <= 2:
        if random.random() < 0.3:
            return [random.choice(config.exclamations)] + tokens
    if len(tokens) >= 3 and sum([len(token) for token in tokens]) >= 20:
        if random.random() < 0.3:
            return tokens + [random.choice(config.exclamations)]
    return tokens


def convert_zenkaku_katakana_to_hankaku(tokens):
    new_tokens = []
    for token in tokens:
        if random.random() < 0.8:
            new_tokens.append(mojimoji.zen_to_han(token))
        else:
            new_tokens.append(token)
    return new_tokens


def add_symbols(tokens):
    prob = 0.2
    new_tokens = []
    if len(tokens) == 1:
        new_tokens.append(tokens[0])
        if random.random() < prob:
            new_tokens.append(symbol_gen())
        return new_tokens

    for token in tokens:
        new_tokens.append(token)
        new_tokens.append(symbol_gen())
    return new_tokens


def generate_sentence_climate(climate):
    prefix = this_is_gen("climate") + decorator_gen()
    climate_phrase = [random.choice(config.climate_phrase[climate])]
    postfix = desune_gen("climate")

    cleaned_phrases = process_tokens(prefix + climate_phrase + postfix)
    return "".join(cleaned_phrases)


def generate_sentence_season(season):
    prefix = this_is_gen("season") + decorator_gen()
    season_phrase = [random.choice(config.season_phrase[season])]
    postfix = desune_gen("season")

    cleaned_phrases = process_tokens(prefix + season_phrase + postfix)
    return "".join(cleaned_phrases)


def this_is_gen(mode) -> list[str]:
    random_num = random.random()

    if mode == "climate":
        if random_num < 0.8:
            return [""]
        else:
            return ["これは"]

    else:
        if random_num < 0.6:
            return ["これは"]
        elif random_num < 0.7:
            return ["これはね"]
        elif random_num < 0.8:
            return ["これはですねえ"]
        else:
            return [""]


def desune_gen(mode) -> list[str]:
    random_num = random.random()

    if mode == "climate":
        return [""]

    else:
        if random_num < 0.1:
            return ["ネ"]
        elif random_num < 0.2:
            return ["です", "ネ"]
        else:
            return [""]


def decorator_gen() -> list[str]:
    decorator = random.sample(
        config.decorators,
        random.choices([0, 1, 2, 3], weights=[20, 5, 2, 1])[0],
    )
    if len(decorator) == 1:
        if random.random() > 0.5:
            decorator[0] = decorator[0] + "ねえ"
    return decorator


def symbol_gen() -> str:
    symbols = random.choice(config.symbols)
    while random.random() > 0.5:
        symbols += random.choice(config.symbols)
    return symbols


for i in range(100):
    text = generate_sentence()
    print(text)
