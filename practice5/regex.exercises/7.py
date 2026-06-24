import re
s = input()
print(re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s))