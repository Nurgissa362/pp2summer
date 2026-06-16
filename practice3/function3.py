def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


def my_function(name):
  print("Hello", name)

my_function("Emil")


def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)