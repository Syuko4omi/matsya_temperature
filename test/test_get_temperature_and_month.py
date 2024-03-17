from matsya_temperature.get_temperature_and_month import (
    get_temperature_and_month,
)


def test_get_temperature_and_month_tokyo():
    apparent_temperature, month = get_temperature_and_month("Tokyo, JP")
    assert apparent_temperature != -1000.0
    assert month != 100


def test_get_temperature_and_month_unknown_place():
    apparent_temperature, month = get_temperature_and_month("aaa")
    assert apparent_temperature == -1000.0
    assert month == 100


test_get_temperature_and_month_tokyo()
