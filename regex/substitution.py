import re

# pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([(a-z])([a-z]+)', re.I)
# text = 'Last night Mrs. Daisy and Mr. White murdered Ms. Chow'
# print(pattern.sub(r'\1 \2.', text))

pattern = re.compile(r'\bfrack[\w]*', re.I)
text = 'I hope you fracked mind'
print(pattern.sub('CENSORED', text))

