import re
s = input()
r = input()
if re.search(r,s):
    print("Yes")
else:
    print("No")