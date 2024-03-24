import random

from matsya_temperature.config import decorators, symbols


def this_is_gen(mode: str) -> list[str]:
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


def desune_gen(mode: str) -> list[str]:
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
        decorators,
        random.choices([0, 1, 2, 3], weights=[20, 5, 2, 1])[0],
    )
    if len(decorator) == 1:
        if random.random() < 0.5:
            return [decorator[0] + "ねえ"]
    return decorator


def symbol_gen() -> str:
    symbols_str = random.choice(symbols)
    while random.random() < 0.5:
        symbols_str += random.choice(symbols)
    return symbols_str
