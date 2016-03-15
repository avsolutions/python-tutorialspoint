# title             : operators.py
# author            : An Bui
# date              : 03/15/2016
# version           : 1.0

# declare variable
number1 = None
number2 = None

# get first number from user
user_input = input("Please enter the first number: ")
if user_input.isnumeric():
    number1 = float(user_input)

# get second number from user
user_input = input("Please enter the second number: ")
if user_input.isnumeric():
    number2 = float(user_input)

# addition of number1 and number2
addition = "%.1f + %.1f = %.1f" % (number1, number2, number1 + number2)
print(addition)

# subtraction of number1 and number2
subtraction = "%.1f - %.1f = %.1f" % (number1, number2, number1 - number2)
print(subtraction)

# multiplication of number1 and number2
multiplication = "%.1f * %.1f = %.1f" % (number1, number2, number1 * number2)
print(multiplication)

# division of number1 and number2
division = "%.1f / %.1f = %.1f" % (number1, number2, number1 / number2)
print(division)

# modulus of number1 and number2
modulus = "%.1f %% %.1f = %.1f" % (number1, number2, number1 % number2)
print(modulus)
