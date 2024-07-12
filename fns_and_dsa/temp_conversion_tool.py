#!/bin/bash

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main function to handle user interaction
def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        if scale == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature} Fahrenheit is {converted_temperature:.2f} Celsius.")
        elif scale == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature} Celsius is {converted_temperature:.2f} Fahrenheit.")
        else:
            print("Invalid scale. Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

