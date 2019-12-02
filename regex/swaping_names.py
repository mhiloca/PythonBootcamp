import re

titles = [
    'Signficant Others (1987)',
    'Tales of the City (1978)',
    'The Day of Ann Madrigal (2014)',
    'Mary Ann in Autumn (2010)',
    'Further Tales of the City (1982)',
    'Babycakes (1984)',
    'More Tales of the City (1980)',
    'Sure of You (1989)',
    'Michael Tolliver Lives (2007)'
]

pattern = re.compile(r'(?P<title>[\w ]+) \((?P<year>\d{4})\)')
res = []
for title in titles:
    res.append(pattern.sub(r'\g<year> - \g<title>', title))
for r in sorted(res):
    print(r)
