import random

import mojimoji

from matsya_temperature.config import exclamations
from matsya_temperature.specific_token_generator import symbol_gen


def process_tokens(tokens: list[str]) -> list[str]:
    step_1 = remove_empty_string_from_list(tokens)
    step_2 = add_exclamation_to_short_or_long_sentence(step_1)
    step_3 = convert_zenkaku_katakana_to_hankaku(step_2)
    step_4 = add_symbols(step_3)
    return step_4


def remove_empty_string_from_list(tokens: list[str]) -> list[str]:
    return list(filter(lambda x: x != "", tokens))


def add_exclamation_to_short_or_long_sentence(tokens: list[str]) -> list[str]:
    if len(tokens) == 1 and len(tokens[0]) <= 2:
        if random.random() < 0.3:
            return [random.choice(exclamations)] + tokens
    if len(tokens) >= 3 and sum([len(token) for token in tokens]) >= 20:
        if random.random() < 0.3:
            return tokens + [random.choice(exclamations)]
    return tokens


def convert_zenkaku_katakana_to_hankaku(tokens: list[str]) -> list[str]:
    new_tokens = []
    for token in tokens:
        if random.random() < 0.8:
            new_tokens.append(mojimoji.zen_to_han(token))
        else:
            new_tokens.append(token)
    return new_tokens


def add_symbols(tokens: list[str]) -> list[str]:
    new_tokens = []
    if len(tokens) == 1:
        new_tokens.append(tokens[0])
        if random.random() < 0.2:
            new_tokens.append(symbol_gen())
        return new_tokens

    for token in tokens:
        new_tokens.append(token)
        new_tokens.append(symbol_gen())
    return new_tokens
