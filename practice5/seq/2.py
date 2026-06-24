import re
s = input()
di = re.findall(r'\d', s)
print(" ".join(di))