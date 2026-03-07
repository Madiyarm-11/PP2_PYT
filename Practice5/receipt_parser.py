import re

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"([A-Za-z ]+)\s+(\d+\.\d{2})"

matches = re.findall(pattern, text)

print("Items in receipt:\n")

for item, price in matches:
    print(f"{item.strip()} -> {price}")