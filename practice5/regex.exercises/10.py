import re
s = input()
print(re.sub(r'([A-Z])', r'_\1', s).lower())