

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))


if unit == "C":
    temperature = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temperature} degrees F ")
elif unit == "F":
    temperature = round((temp - 32) * 5 /9, 1)
    print(f"The temperature in Celsius is: {temperature} degrees C ")

else:
    print(f"{unit} is an invalid unit of measurement")