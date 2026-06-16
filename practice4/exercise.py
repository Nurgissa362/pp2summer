from datetime import datetime, timedelta
import math
import json

# 1
today = datetime.now()
result = today - timedelta(days=5)
print("1:", result)

# 2
today = datetime.now()
print("2:")
print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))

# 3
now = datetime.now()
print("3:", now.replace(microsecond=0))

# 5
date1 = datetime(2026, 3, 1)
date2 = datetime(2026, 2, 28)
difference = abs((date1 - date2).total_seconds())
print("5:", difference)

# 6
def squares(n):
    for i in range(n + 1):
        yield i * i

print("6:")
for num in squares(5):
    print(num)

# 7
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n for task 7: "))
print("7:", ",".join(str(x) for x in even_numbers(n)))

# 8
def divisible(n):
    for i in range(n + 1):
        if i % 12 == 0:  # делится и на 3, и на 4
            yield i

print("8:")
for num in divisible(50):
    print(num)

# 9
def squares_range(a, b):
    for i in range(a, b + 1):
        yield i * i

print("9:")
for x in squares_range(2, 5):
    print(x)

# 10
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("10:")
for num in countdown(5):
    print(num)

# 11
degree = float(input("Enter degree: "))
radian = math.radians(degree)
print("11:", radian)

# 12
height = float(input("Enter height: "))
a = float(input("Enter first base: "))
b = float(input("Enter second base: "))
area = (a + b) * height / 2
print("12:", area)

# 13
base = float(input("Enter base: "))
height = float(input("Enter height: "))
print("13:", base * height)

# 14
try:
    with open("sample-data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    print("14:", data)
except FileNotFoundError:
    print("14: File 'sample-data.json' not found.")