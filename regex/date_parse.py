import re


def parse_date(string):
    date_pattern = re.compile(r'(?P<d>[0-2][0-9]|3[0-1])[.,/](?P<m>0[1-9]|1[0-2])[.,/](?P<y>\d{4})')
    match = date_pattern.fullmatch(string)
    if match:
        match = match.groupdict()
        return match
    return None


date = '19.09.1900'
print(parse_date(date))
