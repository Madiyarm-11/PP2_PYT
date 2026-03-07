import re

a = input().split()
sun=0
for n in a:
    res=len(n)
    if res==3:
        sun+=1
        
print(sun)
        
