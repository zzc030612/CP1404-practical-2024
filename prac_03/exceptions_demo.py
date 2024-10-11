"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when the input for either the numerator or denominator is not a valid integer.
    For example, if the user enters a letter or a symbol instead of a number.
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur when the user enters 0 as the denominator, since division by zero is not allowed in mathematics.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        while denominator == 0:
            print("Denominator cannot be zero.")
            denominator = int(input("Enter the denominator: "))

        fraction = numerator / denominator
        print(fraction)

    except ValueError:
        print("Numerator and denominator must be valid numbers!")

    except ZeroDivisionError:
        print("Cannot divide by zero!")

    print("Finished.")
