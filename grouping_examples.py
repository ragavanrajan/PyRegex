import re
print(re.search(r'abxy?cde', 'abcde')) # None
print(re.search(r'ab(xy)?cde', 'abcde')) # ... match='abcde'
match = re.search(r'a([b-d]*)e', 'abcde')
print(match.group()) # abcde
print(match.group(1)) # bcd