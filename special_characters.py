import re
match = re.search('.', 'abcde')
if match:
    print("found:", match.group())
# found: a
else:
    print("not found")
# backslashes have a special meaning in string literals
# so they need to be escaped
pattern = '\\.'
print(pattern)  # \.
match = re.search(pattern, 'abc.de')
if match:
    print("found:", match.group())
# found: .
else:
    print("not found")

    match = re.search(r'cf|cd', 'abcde')
    if match:
        print("found:", match.group())
    # found: cd
    else:
        print("not found")
