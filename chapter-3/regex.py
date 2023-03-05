import re

# a,b,c
days = r'(Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)day'
nums = r'[0-9][0-9]?[0-9]?(,[0-9][0-9][0-9])*'
emails = r'\"[A-Z][a-z]* [A-Z][a-z]*\" <[a-z]+[a-z0-9]*(\.?[a-z0-9])*@[a-z]+\.com>'

# url regex stuff
domainlabel = r'[a-zA-Z0-9]([a-zA-Z0-9]|-)*[a-zA-Z0-9]'
toplabel = r'[a-zA-Z](([a-zA-Z0-9]|\-)*[a-zA-Z0-9])?'
hostname = rf'({domainlabel}\.)*{toplabel}'
hostnumber = r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
host = rf'({hostname}|{hostnumber})'
port = r'[0-9]+'
hostport = rf'({host})(:{port})?'
safe = r'\$|\-|\_|\.|\+'
extra = r'\!|\*|\'|\(|\)|\,'
unreserved = rf'[a-zA-Z0-9]|({safe})|({extra})'
reserved = r'\;/\?\:\@\&\='
hex = r'[a-fA-F0-9]'
escape = rf'\%({hex})({hex})'
uchar = rf'({unreserved})|({escape})'
xchar = rf'({unreserved})|({escape})|({reserved})'

# http
hsegment = rf'(({uchar})|\;|\:|\@|\&|\=)*'
search = rf'(({uchar})|\;|\:|\@|\&|\=)*'
hpath = rf'{hsegment}(/({hsegment}))*'
http = rf'https?://({hostport})(/{hpath}(\?{search})?)?'

# gopher
gtype = xchar
selector = rf'({xchar})*'
gopherstr = rf'({xchar})*'
gopher = rf'gopher://({hostport})(/(({gtype})(({selector})((\%09{search})(\%09{gopherstr})?)?)?)?)?'

# file
fsegment = rf'(({uchar})|\?|\:|\@|\&|\=)*'
fpath = rf'({fsegment})(/({fsegment}))*'
file = rf'file://({host}|localhost)?/({fpath})'

# url
urls = rf'{http}|({gopher})|({file})'

# X<>{}
brackets = r'\{X*(\<X*\>)*X*\}'
carots = r'\<X*(\{X*\})*X*\>'
xxx = rf'(X*(({carots})|({brackets}))*X*)+'

# test days
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
regex = re.compile(days)
for day in days_of_week:
  assert regex.fullmatch(day)
  assert not regex.fullmatch(day[:-3])
  assert not regex.fullmatch(day.lower())
assert not regex.fullmatch('Notaday')
print('days test succesful')

# test nums
regex = re.compile(nums)
assert regex.fullmatch('1,234,567')
assert regex.fullmatch('1')
assert regex.fullmatch('12')
assert regex.fullmatch('123')
assert not regex.fullmatch('1234')
assert not regex.fullmatch('1234,123')
assert regex.fullmatch('1,234')
assert not regex.fullmatch('1,2345')
print('nums test succesfull')

# test emails
regex = re.compile(emails)
assert regex.fullmatch('"John Doe" <john.doe@gmail.com>')
assert regex.fullmatch('"King Charles" <kingc420@castle.com>')
assert not regex.fullmatch("<email@email.com>")
assert not regex.fullmatch('"Email Man"')
assert not regex.fullmatch('"Email Man" <@email.com>')
print('emails test successful')

# test urls
regex = re.compile(urls)
assert regex.fullmatch('http://replit.com/@bradley-ray/compilerbook-solutions')
assert regex.fullmatch('file:///home/bradley/Documents/books/introduction-to-compilers-and-language-design.pdf')
assert regex.fullmatch('gopher://gopher.floodgap.com')
assert not regex.fullmatch('://aksfksdljfa.com/akdf;j')
print('urls test successful')

# test X<>{}
regex = re.compile(xxx)
assert regex.fullmatch('XXX<XX{X}XXX>X')
assert regex.fullmatch('X{X}X<X>X{X}X<X>X')
assert not regex.fullmatch('XXX<X<XX>>XX')
assert not regex.fullmatch('XX<XX{XX>XX}XX')
print('X<>{} test successful')
