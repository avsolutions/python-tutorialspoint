# title             : lists.py
# description       :
# author            : An Bui
# date              : 03/19/2016
# version           : 1.0

# declare variables
is_digit = False
list_items = []
user_input = ""
# check user input for number of elements
# condition: the value must be an integer and less than 10
while is_digit == False:
    user_input = str(input("Please enter number of elements (n<10):"))
    is_digit = user_input.isdigit()
number_elements = int(user_input)

# user input value for list
for index in range(0, number_elements):
    tmp = "Item %d: " % index
    val_input = str(input(tmp))
    list_items.append(val_input)

# print list
print("Your list:", list_items)
print("Length of list:", len(list_items))
if list_items.count('3'):
    print("Number 3 is in this list")
else:
    print("Number 3 is out of this list")
