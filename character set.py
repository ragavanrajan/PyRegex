import re
print(re.findall(r'[af]', 'abc123def'))
print(re.findall(r'[a-z]', 'abc123def'))

# ^, $ (positioning/anchors)
print("Postioning Anchors")
print(re.search(r'^cd', 'abcde'))
print(re.search(r'^ab', 'abcde'))
print(re.search(r'^ab$', 'abcde'))
print(re.search(r'^ab$', 'ab'))