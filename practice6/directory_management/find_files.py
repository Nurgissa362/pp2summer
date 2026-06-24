import os
files = os.listdir(".")
txt_files = [f for f in files if f.endswith]
print("TXT files")
for file in txt_files:
    print(file)