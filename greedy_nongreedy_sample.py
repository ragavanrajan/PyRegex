import re
print(re.search(r'<.*>', '<p>hello</p><p>world</p>'))
# ... match='<p>hello</p><p>world</p>'
print(re.search(r'<.*?>', r'<p>hello</p><p>world</p>'))
# ... match='<p>'
print(re.search(r'<p>.*?</p>', r'<p>hello</p><p>world</p>'))
# ... match='<p>hello</p>'