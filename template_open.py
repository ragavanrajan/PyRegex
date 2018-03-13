import re

# open the input file for reading
file = open('mountain.html', encoding="UTF-8")
# read the entire file
text = file.read()
# split into lines
lines = text.splitlines()
print("0. Example: All tags.")
matches = re.findall(r'<[^>]+>', text)
for s in matches:
    print(s)
print("total:", len(matches))
