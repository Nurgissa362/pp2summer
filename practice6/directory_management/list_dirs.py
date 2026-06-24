import os
items = os.listdir(".")
print("Files and folders in current directory:")
for item in items:
    print(item)