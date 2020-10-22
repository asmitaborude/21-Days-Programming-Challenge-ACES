#get current date and time
import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)

#get current date
import datetime

date_object = datetime.date.today()
print(date_object)

#whats inside datetime
import datetime

print(dir(datetime))

#date object to represent a date
import datetime

d = datetime.date(2019, 4, 13)
print(d)

#get date from a timestamp
from datetime import date

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

#time object to represent time
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

#print hour,minute,second and microsecond
from datetime import time

a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)

#python datetime object
from datetime import datetime

#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

#Print year, month, hour, minute and timestamp
from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

