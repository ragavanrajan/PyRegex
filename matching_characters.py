#!/usr/bin/python3
import re

pattern = 'cd'
input = 'abcde'
match = re.search(pattern, input)
if match != None:
    print("found:", match.group())
    # found: cd
else:
    print("not found")

# metacharacters
match = re.search('.', 'abcde')
if match:
    print("found:", match.group())
# found: a
else:
    print("not found")

match = re.search('ad', 'abcde')
print(match)