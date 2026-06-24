import re
s = input()
print(re.sub(r'([A-Z])', r' \1', s).strip())