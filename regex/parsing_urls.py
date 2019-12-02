import re

url_pattern = re.compile(r'(https?)://(\w{3,}\.[A-Za-z-]{2,256}\.[a-z]{2,6})[-a-zA-Z0-9@:%_+.~#?&/=]*')
match = url_pattern.search('https://www.udemy.com/the-modern-python3-bootcamp/'
                              'learn/lecture/9328506#announcements/2440988')
print(match.groups())
print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(2))
