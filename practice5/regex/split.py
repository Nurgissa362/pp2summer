import re
s = input()
p = input()
parts = re.split(p, s)
print(",".join(parts))