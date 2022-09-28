"""Test converters.

length_units    = [millimeter, centimeter, meter, kilometer]
area_units      = [millimeters_squared, centimeters_squared,
              meters_squared, kilometers_squared]
volume_units    = [millimeters_cubed, centimeters_cubed,
                milliliter, liter, meters_cubed, kilometers_cubed]
pressure_units  = [pascal, kilopascal, megapascal, gigapascal, bar, atm]
energy_units    = [joule, kilojoule, megajoule]
time_units      = [seconds, milliseconds, minutes, hours]
"""
import pytest
from convert import convert_unit, units


@pytest.mark.parametrize('value, original_unit, converted_unit ,result', [
    (60, units[5][0], units[5][2], 1),
])
def test_time_converter(value, original_unit, converted_unit, result):
    """Test time conversions."""
    assert convert_unit(value, original_unit, converted_unit) == result
