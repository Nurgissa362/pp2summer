import re
import os

filename = "raw.txt"

if not os.path.exists(filename):
    print(f"Файл {filename} не найден!")
    print("Создайте файл raw.txt в папке:", os.getcwd())
    exit()

with open(filename, encoding="utf-8") as f:
    text = f.read()

products = re.findall(r'^\d+\.\s*(.+?)$', text, re.MULTILINE)
prices = re.findall(r'(\d+[\d.]*,\d{2})', text)
date = re.search(r'(\d{2}\.\d{2}\.\d{4})\s\d{2}:\d{2}:\d{2}', text)
total = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', text)
payment = re.search(r'(Банковская карта)', text)

print("Products:")
for p in products:
    print(f"  - {p}")

print("\nPrices:")
for p in prices:
    print(f"  - {p}")

print(f"\nTotal: {total.group(1).strip() if total else 'Не найдено'}")
print(f"Date: {date.group(1) if date else 'Не найдено'}")
print(f"Payment: {'Да' if payment else 'Нет'}")