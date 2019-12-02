import re

phone_pattern = re.compile(r'(\d{3} \d{3}-?\d{4})')
res = phone_pattern.findall('Call me at 451 555-4242 or 322 342-8923')
for phone in res:
    print(phone)
