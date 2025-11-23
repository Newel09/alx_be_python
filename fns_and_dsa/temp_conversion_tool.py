FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0        # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0        # Conversion factor from Celsius to Fahrenheit
FAHRENHEIT_TO_CELSIUS_OFFSET = 32               # Offset for Fahrenheit to Celsius conversion

def convert_to_fahrenheit(celsius):             # Convert Celsius to Fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_TO_CELSIUS_OFFSET

def convert_to_celsius(fahrenheit):             # Convert Fahrenheit to Celsius 
    return (fahrenheit - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

while True:                                     # Main loop for user interaction
    print("_____Temperature Conversion Tool_____")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")
    user_choice = input("Choose an option (1-3): ")

    if user_choice == '1':
        celsius_input = input("Enter temperature in Celsius: ")
        try:
            celsius = float(celsius_input)
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius} C is {fahrenheit:.2f} F\n")
        except ValueError:
            print("Please enter a valid number for Celsius temperature.\n")
    elif user_choice == '2':
        fahrenheit_input = input("Enter temperature in Fahrenheit: ")
        try:
            fahrenheit = float(fahrenheit_input)
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit} F is {celsius:.2f} C\n")
        except ValueError:
            print("Please enter a valid number for Fahrenheit temperature.\n")
    elif user_choice == '3':
        print("Exiting the Temperature Conversion Tool. Goodbye!")
        break