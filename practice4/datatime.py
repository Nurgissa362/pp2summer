numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

import datetime

x = datetime.datetime(2018, 7, 1)

print(x.strftime("%B"))

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

import datetime

x = datetime.datetime.now()

print(x.year)