import re
s = input()
print(bool(re.fullmatch(r'ab{2,3}', s)))