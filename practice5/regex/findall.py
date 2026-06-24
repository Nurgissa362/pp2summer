import re
s = input()
p = input()
findall = re.findall(p,s)
print(len(findall))