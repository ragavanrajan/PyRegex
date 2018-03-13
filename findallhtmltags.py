import re

html = '<h1>Hi</h1><p>Good <span class="time">morning</span></p>'
matches = re.findall(r'<[^>]+>', html)
for s in matches:
    # print in the same line use end='' 
    print(s, end='')
