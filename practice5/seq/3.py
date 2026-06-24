import re
s = input()
if re.search(r'^[A-Za-z].', s):
    print("Yes")
else:
    print("No")