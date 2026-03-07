import re
a=input().strip()
b=input()
c=input()
match=re.sub(re.escape(b),c, a)
print(match)

