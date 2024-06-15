def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return celsius_to_fahrenheit(value)
        elif to_unit == "kelvin":
            return celsius_to_kelvin(value)
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return fahrenheit_to_celsius(value)
        elif to_unit == "kelvin":
            return fahrenheit_to_kelvin(value)
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return kelvin_to_celsius(value)
        elif to_unit == "fahrenheit":
            return kelvin_to_fahrenheit(value)
    return None

def display_conversions(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    return (f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit "
            f"and {kelvin} degrees Kelvin.")

# Test the function
input_celsius = 20
output = display_conversions(input_celsius)
print(output)