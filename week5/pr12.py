import re

text = input().strip()

wb= re.findall(r'\d+', text)
for i in wb:
    if int(i)>=10:
        print(i, end=" ")
   