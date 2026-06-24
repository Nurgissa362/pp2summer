import re
s = input()
print(bool(re.fullmatch(r'ab*', s)))