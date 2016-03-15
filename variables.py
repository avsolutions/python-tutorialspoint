# title             : variables.py
# description       :
# author            : An Bui
# date              : 03/15/2016
# version           : 1.0

# assign value to variable

# try to enter an integer number
user_input = input("Please enter an integer number: ")
try:
    my_int = int(user_input)
except ValueError:
    print(user_input, "is not an integer number!")
else:
    print("Your integer number:", my_int)

# try to enter an float number
user_input = input("Please enter an float number: ")
try:
    my_float = float(user_input)
except ValueError:
    print(user_input, "is not an float number!")
else:
    print("Your float number:", my_float)

# try to enter an string value
user_input = input("Please enter your name: ")
my_str = user_input
print("Your name:", my_str)
