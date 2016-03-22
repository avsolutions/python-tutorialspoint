# title             : function.py
# description       :
# author            : An Bui
# date              : 03/22/2016
# version           : 1.0

# printme function
def printme(str):
    print(str)
    return


# pass by reference
def changeme(mylist):
    mylist.append("12")
    mylist.append("234")
    print(mylist)
    return


# change local variable
def changelocal(mylist):
    mylist = ["item-new-1", "item-new-2", "item-new-3"]
    print(mylist)
    return


mylist = [1, 2, 3]
changeme(mylist)
print(mylist)

mynewlist = ["item1", "item2", "item3"]
changelocal(mynewlist)
print(mynewlist)

# function arguments
# 1. Required argument
# printme need to be passed an argument, so when calling the following function,
# a error will happen
# printme()

# 2. Keyword argument
printme(str="Bui Thien An")


# 3. Default argument
def printinfo(name, age=27):
    print("Name:", name)
    print("Age:", age)
    return


printinfo("Nguyen Thanh Thoai Van")
printinfo("Nguyen THanh THoai Long", 24)


# 4. Variable-length argument
def printinfo2(name, *unknowvar):
    print("The info is:")
    print(name)
    for var in unknowvar:
        print(var)


printinfo2("An")
printinfo2("Van", 34, "TMA")
printinfo2("Long", "CSC", 17, "Hutech")

# 5. The Anonymous Functions, Using lambda keywords
sumfunc = lambda var1, var2: var1 + var2
print(sumfunc(1, 2))
