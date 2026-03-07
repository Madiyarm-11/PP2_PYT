import re
a=input()
res = re.match("Hello", a)
if res:
    print("Yes")
else:
    print("No")