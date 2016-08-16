"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Lindsay Ward'


def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            conv_to_celsius()
        elif choice == "F":
            conv_to_fahrenheit()
            # TODO: Write this section so the program converts F to C and displays the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def conv_to_celsius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def conv_to_fahrenheit():
    fahrenheit = float(input("fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} F".format(celsius))

main()