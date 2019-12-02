import re


name_pattern = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Z][a-z]+) (?P<last_name>[A-Z][a-z]+)$')
match = name_pattern.search('Mrs. Tilda swinton'.title())
print(match.groups())