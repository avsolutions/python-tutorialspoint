# title             : date-time.py
# description       :
# author            : An Bui
# date              : 03/22/2016
# version           : 1.0

# import time module
import calendar
import time

# print currently time
ticks = time.time()
localtime = time.localtime(ticks)
print("Year:", localtime[0])
print("Month:", localtime[1])
print("Day:", localtime[2])
print("Hour:", localtime[3])
print("Minute:", localtime[4])
print("Second:", localtime[5])
print("Days of week:", localtime[6])
print("Days of month:", localtime[7])
print("Saving time:", localtime[8])

# print calendar for a month
print("Calendar for this month")
cal = calendar.month(localtime[0], localtime[1])
print(cal)
