import re
a=input()

if re.fullmatch(r"[A-Za-z]+\d+", a):
    print("Yes")
else:
    print("No")

