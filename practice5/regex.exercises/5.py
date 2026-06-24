import re
s = input()
print(bool(re.search(r'a.*b', s)))