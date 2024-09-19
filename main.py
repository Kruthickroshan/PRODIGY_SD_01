def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    c = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(c)

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    c = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c)

def main():
    print("Temperature Converter")
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature} °C = {fahrenheit:.2f} °F")
        print(f"{temperature} °C = {kelvin:.2f} K")

    elif unit == 'F':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature} °F = {celsius:.2f} °C")
        print(f"{temperature} °F = {kelvin:.2f} K")

    elif unit == 'K':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"{temperature} K = {celsius:.2f} °C")
        print(f"{temperature} K = {fahrenheit:.2f} °F")

    else:
        print("Invalid unit. Please enter C, F, or K.")

if __name__ == "__main__":
    main()
