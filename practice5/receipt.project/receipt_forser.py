import re
import json
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()
prices = re.findall(r'\d+\s*x\s*([\d\s]+,\d{2})', text)
prices = [p.replace(" ", "").replace(",", ".") for p in prices]
product_pattern = r'\d+\.\n(.+)'
products = re.findall(product_pattern, text)
total_match = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', text)
total = total_match.group(1).replace(" ", "").replace(",", ".") if total_match else None
datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2})', text)
datetime = datetime_match.group(1) if datetime_match else None
payment_match = re.search(r'(Банковская карта|Наличные)', text)
payment_method = payment_match.group(1) if payment_match else None
data = {
    "products": products,
    "prices": prices,
    "total_amount": total,
    "datetime": datetime,
    "payment_method": payment_method
}
print(json.dumps(data, indent=4, ensure_ascii=False))