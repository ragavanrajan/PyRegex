import re

print(re.search(r'a*', 'aaabbb'))
print(re.search(r'x*', 'aaabbb'))
print(re.search(r'a+', 'aaabbb'))
print(re.search(r'x+', 'aaabbb'))
print(re.search(r'a?', 'aaabbb'))
print(re.search(r'ba?', 'aaabbb'))
print(re.search(r'a{1,20}', 'aaabbb'))
print(re.search(r'a{2}', 'aaabbb'))