# title             : strings.py
# description       :
# author            : An Bui
# date              : 03/19/2016
# version           : 1.0

# input a given string
str_len = 0
while str_len < 10:
    str = input("Please enter a string with more than 10 characters:")
    str_len = len(str)
print("Your string:", str)
print("The first character:", str[0])
print("The last character:", str[-1])
print("The characters start from 2rd", str[1:])
print("The characters start from 2rd to before the last character", str[1:-1])
print("The double string:", str * 2)

# built-in string method
print("Number of e character in the string:", str.count("e"))
print("String length:", len(str))
print("UPPER string:", str.upper())
print("LOWER string:", str.lower())
