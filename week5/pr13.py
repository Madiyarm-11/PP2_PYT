import re

text = input().strip()

wb= re.findall(r'\w+', text)
sun=len(wb)
print(sun)