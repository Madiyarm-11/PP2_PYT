import re

text = input().strip()

pattern = r'Name:\s*(.+?),\s*Age:\s*(\d+)'

match = re.search(pattern, text)
if match:
    print(f"{match.group(1)} {match.group(2)}")