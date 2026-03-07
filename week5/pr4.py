import re
a=input()

res = re.findall(r"\d", a)
for n in res:
    print(n, end=" ")
