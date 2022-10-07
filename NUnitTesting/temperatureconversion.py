def celsius_conversion(x):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def fahrenheit_conversion(y):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


if __name__ == "__main__":
    print("Enter choice of Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input())
    if (choice == 1):
        print("Enter temperature in celsius ")
        celsius = int(input())
        output1 = fahrenheit_conversion(celsius)
        print("Temperature in Fahrenheit :", output1)
    else:
        print("Enter temperature in fahrenheit")
        fahrenheit = int(input())
        output2 = celsius_conversion(fahrenheit)
        print("Temperature in Celsius: ", output2)


# def test_celsius_conversion(self):
#     fahrenheit = 45
#     result = celsius_conversion(x)
#     self.assertEqual(result, celsius)


# if __name__ == "__main__":
#     test_celsius_conversion()
