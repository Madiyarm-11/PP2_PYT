import re
a=input()
b=input()
res = re.search(b, a)
if res:
    print("Yes")
else:
    print("No")