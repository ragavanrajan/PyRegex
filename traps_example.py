import re
# bad attempt to match div tag with id="hello"
print(re.search(r'<div.*?id="hello".*?>', '<div><div id="hello"></div></div>'))
# ... match='<div><div id="hello">'
# improved
print(re.search(r'<div[^>]*id="hello"[^>]*>', '<div><div id="hello"></div></div>'))
# ... match='<div id="hello">'