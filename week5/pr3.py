import re
a=input()
b=input()
res = re.findall(b, a)
print(len(res))
