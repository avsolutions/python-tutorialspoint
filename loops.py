# title             : loops.py
# description       :
# author            : An Bui
# date              : 03/19/2016
# version           : 1.0

# while loop
count = 0
while (count < 9):
    print(count)
    count += 1
print("End of while loop!!!")

# while loop with else
count = 0
while (count < 5):
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is equal with 5")
print("End of while loop with else!!!")

# for loop
users = ["user1", "user2", "user3", "user4"]
for user in users:
    print("User:", user)

# for loop with range
print("For loop use index")
for index in range(len(users)):
    print("User:", users[index])

#
for num in range(10, 20):
    for id in range(2, num):
        if num % id == 0:
            j = num / id
            print(num, "equals", id, "*", j)
            break
    else:
        print(num, "is a prime number")
