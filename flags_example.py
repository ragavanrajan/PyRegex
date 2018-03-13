import re
print(re.search(r'.*', 'aB\ncD')) # ... match='aB'
print(re.search(r'.*', 'aB\ncD', re.S)) # ... match='aB\ncD'
print(re.search(r'ab$', 'aB\ncD')) # None
print(re.search(r'ab$', 'aB\ncD', re.I|re.M))# ... match='aB'`