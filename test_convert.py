"""Test converters.

time_units      = [seconds, milliseconds, minutes, hours]
length_units    = [millimeter, centimeter, meter, kilometer]
area_units      = [millimeters_squared, centimeters_squared,
              meters_squared, kilometers_squared]
volume_units    = [millimeters_cubed, centimeters_cubed,
                milliliter, liter, meters_cubed, kilometers_cubed]
pressure_units  = [pascal, kilopascal, megapascal, gigapascal, bar, atm]
energy_units    = [joule, kilojoule, megajoule]
"""
import pytest
from convert import convert_unit, units


@pytest.mark.parametrize('value,original_unit,converted_unit,result', [
    (60, units[0][0], units[0][2], 1),
    (2, units[0][3], units[0][2], 120),
    (1, units[0][2], units[0][1], 60000),
])
def test_time_converter(value, original_unit, converted_unit, result):
    """Test time conversions."""
    assert convert_unit(value, original_unit, converted_unit) == result

@pytest.mark.parametrize('value,original_unit,converted_unit,result', [
    (1, units[1][3], units[1][2], 1000),
    (1, units[1][2], units[1][0], 1000),
    (2, units[1][3], units[1][0], 2000000),
])
def test_length_converter(value, original_unit, converted_unit, result):
    """Test length conversions."""
    assert convert_unit(value, original_unit, converted_unit) == result
