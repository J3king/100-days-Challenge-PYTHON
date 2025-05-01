# This is a simple temperature converter that converts between Celsius, Fahrenheit, and Kelvin.
# It provides a command-line interface for the user to select the conversion type and input the temperature value.
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def main():
    print("=== Temperature Converter ===")
    print("Available conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = input("Enter the conversion number (1-6): ")

    temp = float(input("Enter the temperature value: "))
    
    if choice == '1':
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == '2':
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")
    elif choice == '3':
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C = {result:.2f}K")
    elif choice == '4':
        result = kelvin_to_celsius(temp)
        print(f"{temp}K = {result:.2f}°C")
    elif choice == '5':
        result = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F = {result:.2f}K")
    elif choice == '6':
        result = kelvin_to_fahrenheit(temp)
        print(f"{temp}K = {result:.2f}°F")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
