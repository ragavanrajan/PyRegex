# regex library
import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

print(data)

last_name = r'Love'
first_name = r'Kenneth'
# The reason why r is in the front- It tells python it is a raw string
print(re.match(r'Love', data))
# here it doesnt match Kenneth in the file, because it comes after the word 'Love, '
print(re.match(r'Kenneth', data))
# so use search instead of match
print(re.search(r'Kenneth', data))

# Alternative method using variables
print("****Alternative method using variables***:")
print(re.match(last_name, data))
print(re.search(first_name, data))

# matching phone numbers
print("**matching phone numbers***")
print(re.search(r'\d\d\d-\d\d\d\d', data))
# matching phone numbers with paranthesis
print("**matching phone numbers with paranthesis***")
# paranthesis in regex has a special meaning they defined a group. To act as paranthesis u have to escape them
# add forward slash \
print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))

# using Count
# findall is to find in complete file -less readable
# word that occurs with(any sort of unicode characters and underscore , one or more word characters
print(re.findall(r'\w+, \w+', data))
# adding astersik 0 or infinity number of times
print("***adding astersik 0 or infinity number of times:***" )
print(re.findall(r'\w*, \w*', data))
# by adding ? it is optional (0 or 1 times) -? (hypen optional=555 555-5555) /s?(space optional=555-555-5555
print("*****findall using number regex")
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

# using sets
# adding + after the square bracket is we want multiples of any of those to show up
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+',data))
# finding specific text "treeehouse" with sets. re.I indicates Ignorecase
print(re.findall(r'[trehous]+',data,re.I))
# if you want to search for the standalone word "treehouse" then use the word boundaries \b
print("Using Boundaries")
print(re.findall(r'\b[trehous]+\b',data,re.I))
# if you know the length or count of the word "treehouse" then use the {} instead of + sign after the set
print("Using length")
print(re.findall(r'\b[trehous]{9}\b',data,re.I))

# using negations
# match all the email address but ignore .gov email address

print("********ignore .gov email address******")
print(re.findall(r'''
    \b@[-\w\d.]* # First a word boundary, an @ and then any number of characters
      [^\sgov]+ #ignore 1+ more instances of the letters 'g' 'o' or 'v' and a space. since there is a space in the data u have to add \s.
      \b # Match another word boundary
      ''', data, re.VERBOSE | re.I))  # if u r using multiple lines then use VERBOSE

#verbose flag -sample2
# find name and job
print("********find name and job******")
print(re.findall(r"""
      \b[-\w]+ # find a word boundary, 1+ hyphens or characters, and a comma
      \s #find 1 white space
      [-\w ]+ # 1+ hyphens and characters and explicit spaces
      [^\t\n] #ignore tabs and newlines
      """, data, re.X)) #re.X is the shorthand version of verbose flag

# Making groups
print("************Making Groups**********")
# re.multiline is for considering one line treat each line is \n is the end of string
# re.M is alternative
# ^ caret means begining of the string, $means end of the string
print(re.findall(r'''
    ^([-\w ]*,\s[-\w ]+)\s # Last and first names
    ([-\w\d.+]+@[-\w\d.]+)\s #Email
    (\(?\d{3}\)?-?\s?\d{3}-\d{4})?\s #phone numbers
    ([\w\s]+,\s[\w\s.]+)\s? #Job and company
    (@[\w\d]+?)$ #Twitter
''',data, re.X | re.MULTILINE))
# print("********only phone numbers")
# print(re.findall(r'''
#      ([-\w ]*,\s[-\w ]+)\s
#      ''',data, re.X | re.MULTILINE))

# Turn tuples in to dictionary
print("************Making Groups using tuples**********")
line = re.search(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\s # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\s #Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\s #phone numbers
    (?P<job>[\w\s]+,\s[\w\s.]+)\s? #Job and company
    (?P<twitter>@[\w\d]+?)$ #Twitter
    ''',data, re.X | re.M)
print(line)
# groupdict will convert tuple in to dictionary
print(line.groupdict())

# Save pattern using compile- take the regex compile it and ready for use
# u have to take out data when u r compiling it
print("************using compile pattern **********")
line = re.compile(r'''
    ^(?P<name>(?P<first>[-\w ]*),\s(?P<last>[-\w ]+))\s # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\s # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\s # Phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\s? # Job and company
    (?P<twitter>@[\w\d]*)?$ # Twitter handle
''', re.X|re.M)
# to get only one search
# print(line.search(data).groupdict())
# finditer()- gives it back iterable of each non overlapping match- we get back the match objects instead of tuples like re.match or re.search

for match in line.finditer(data):
    # print(match.group('name'))
    # format(**match.groupdict- find those keys as keyword arguments)
    print('{first} {last} <{email}>'.format(**match.groupdict()))