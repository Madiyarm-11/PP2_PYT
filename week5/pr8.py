import re

a = input().strip()
b = input()

match = re.split(b, a)

print(",".join(match))