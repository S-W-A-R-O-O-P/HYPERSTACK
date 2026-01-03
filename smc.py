print("SMART UNIT CONVERTER")
print("----------------------")
print("Choose conversion type:")
print("1. Length")
print("2. Weight")
print("3. Temperature")

choice = input("Enter choice (1/2/3): ")

value = float(input("Enter value: "))

if choice == "1":
    print("\nLength Conversion")
    print("Meters      :", value)
    print("Kilometers  :", value / 1000)
    print("Centimeters :", value * 100)
    print("Millimeters :", value * 1000)

elif choice == "2":
    print("\nWeight Conversion")
    print("Kilograms :", value)
    print("Grams     :", value * 1000)
    print("Pounds    :", value * 2.20462)

elif choice == "3":
    print("\nTemperature Conversion")
    print("Celsius    :", value)
    print("Fahrenheit :", (value * 9/5) + 32)
    print("Kelvin     :", value + 273.15)

else:
    print("Invalid choice")