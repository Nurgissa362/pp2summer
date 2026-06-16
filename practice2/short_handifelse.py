a = 5
b = 2
if a > b: print("a is greater than b")


a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

username = "Tobias"
password = "secret123"
is_verified = True
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")