class unit:
    def __init__(self, unit_type, name, short_name, SI_factor):
        self.type = unit_type
        self.name = name
        self.short_name = short_name
        self.SI_factor = SI_factor

# - - - - - - - - - - - - - - - - - -
# UNIT DEFINITIONS
# - - - - - - - - - - - - - - - - - -


# TIME
seconds = unit("time", "seconds", "s", 1)
milliseconds = unit("time", "milliseconds", "ms", 0.001)
minutes = unit("time", "minutes", "min", 60)
hours = unit("time", "hours", "h", 3600)

time_units = [seconds, milliseconds, minutes, hours]

units = [time_units]


def convert_unit(value, original_unit, converted_unit):
    global units

    for unit_list in units:
        for j in unit_list:
            if original_unit == j.short_name or original_unit == j.name:
                original_unit = j

    for unit_list in units:
        for j in unit_list:
            if converted_unit == j.short_name or converted_unit == j.name:
                converted_unit = j

    if not original_unit.type == converted_unit.type:
        print("ERROR: Incompatible unit types for conversion, can't convert " + original_unit.name + " (" +
              original_unit.short_name + ") to " + converted_unit.name + " (" + converted_unit.short_name + ").")
        return None

    if not original_unit.type == "temperature":
        return value * (original_unit.SI_factor / converted_unit.SI_factor)
    else:
        pass


def main():
    original_unit = input('Enter original unit: ')
    value = float(input('Enter value: '))
    converted_unit = input('Enter converted unit: ')
    print(convert_unit(value, original_unit, converted_unit))


if __name__ == "__main__":
    main()
