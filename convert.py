"""Convert code."""


class Unit:
    """Unit class."""

    def __init__(self, unit_type, name, short_name, si_factor):
        """__init__ function."""
        self.type = unit_type
        self.name = name
        self.short_name = short_name
        self.si_factor = si_factor

# - - - - - - - - - - - - - - - - - -
# UNIT DEFINITIONS
# - - - - - - - - - - - - - - - - - -


# TIME
seconds = Unit("time", "seconds", "s", 1)
milliseconds = Unit("time", "milliseconds", "ms", 0.001)
minutes = Unit("time", "minutes", "min", 60)
hours = Unit("time", "hours", "h", 3600)

# LENGTH
millimeter = Unit("length", "millimeter", "mm", 1/1000)
centimeter = Unit("length", "centimeter", "cm", 1/100)
meter = Unit("length", "meter", "m", 1)
kilometer = Unit("length", "kilometer", "km", 1000)

# AREA
millimeters_squared = Unit("area", "millimeters squared", "mm2", 1/1000000)
centimeters_squared = Unit("area", "centimeters squared", "cm2", 1/10000)
meters_squared = Unit("area", "meters squared", "m2", 1)
kilometers_squared = Unit("area", "kilometers squared", "km2", 1000000)

# VOLUME
millimeters_cubed = Unit("volume", "millimeters cubed", "mm3", 1/1000000000)
centimeters_cubed = Unit("volume", "centimeters cubed", "cm3", 1/1000000)
milliliter = Unit("volume", "milliliter", "mL", 1/1000000)
liter = Unit("volume", "liter", "L", 1/1000)
meters_cubed = Unit("volume", "meters cubed", "m3", 1)
kilometers_cubed = Unit("volume", "kilometers cubed", "km3", 1000000000)

# PRESSURE
pascal = Unit("pressure", "pascal", "Pa", 1)
kilopascal = Unit("pressure", "kilopascal", "kPa", 1000)
megapascal = Unit("pressure", "megapascal", "MPa", 1000000)
gigapascal = Unit("pressure", "gigapascal", "GPa", 1000000000)
bar = Unit("pressure", "bar", "bar", 100000)
atm = Unit("pressure", "atmosphere", "atm", 101325)

# ENERGY
joule = Unit("energy", "joule", "J", 1)
kilojoule = Unit("energy", "kilojoule", "kJ", 1000)
megajoule = Unit("energy", "megajoule", "MJ", 1000000)

time_UNITS = [seconds, milliseconds, minutes, hours]
length_UNITS = [millimeter, centimeter, meter, kilometer]
area_UNITS = [millimeters_squared, centimeters_squared,
              meters_squared, kilometers_squared]
volume_UNITS = [millimeters_cubed, centimeters_cubed,
                milliliter, liter, meters_cubed, kilometers_cubed]
pressure_UNITS = [pascal, kilopascal, megapascal, gigapascal, bar, atm]
energy_UNITS = [joule, kilojoule, megajoule]

UNITS = [time_UNITS, length_UNITS, area_UNITS,
         volume_UNITS, pressure_UNITS, energy_UNITS]


def convert_unit(value, original_unit, converted_unit):
    """convert_unit function."""
    for unit_list in UNITS:
        for j in unit_list:
            if original_unit == j.short_name or original_unit == j.name:
                original_unit = j

    for unit_list in UNITS:
        for j in unit_list:
            if converted_unit == j.short_name or converted_unit == j.name:
                converted_unit = j

    if not original_unit.type == converted_unit.type:
        print("ERROR: Incompatible Unit types for conversion,\
             can't convert " + original_unit.name + " (" +
              original_unit.short_name + ") to " + converted_unit.name +
              " (" + converted_unit.short_name + ").")
        return None

    if not original_unit.type == "temperature":
        return value * (original_unit.si_factor / converted_unit.si_factor)
    else:
        pass


def main():
    """Main's function."""
    original_unit = input('Enter original Unit: ')
    value = float(input('Enter value: '))
    converted_unit = input('Enter converted Unit: ')
    print(convert_unit(value, original_unit, converted_unit))


if __name__ == "__main__":
    main()
