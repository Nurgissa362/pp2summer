import re
s = input()
print(re.findall(r'[a-z]+_[a-z]+', s))