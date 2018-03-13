import re
print(re.sub('bad', 'good', 'bad weather'))
# good weather
print(re.sub(r'colou?rs', r'end', 'the colours of the rainbow'))
# the end of the rainbow
print(re.sub(r'(\d+) dollar[s]? (\d+) cent[s]?', r'$\1.\2', '1 dollar 20 cents'))
# $1.20
print(re.sub(r'(\S{,3})\S*@(\S+)', r'\1...@\2', 'john.smith@example.com'))
# joh...@example.com
print(re.sub(r'((a)b)', r'\1 \2', 'ab'))
# ab a