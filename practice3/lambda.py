x = lambda a, b : a * b
print(x(5, 6))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(11))



numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)