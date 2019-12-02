import re


def extract_phone(text):
    phone_pattern = re.compile(r'(\b(\(?0?\d{2}|(\+|\d+) ?\(?0?\d{2}\)?) ?\d{4,}-? ?\d{4}\b)')
    match = phone_pattern.findall(text)
    try:
        return match
    except AttributeError:
        return '\033[31mInvalid phone number\033[m'
    # if match:
    #     return match.group()
    # return None


def is_valid_phone(string):
    phone_pattern = re.compile(r'^((\(?0?\d{2}|(\+|\d+) ?\(?0?\d{2}\)?) ?\d{4,}-? ?\d{4})$')
    match = phone_pattern.fullmatch(string)
    if match:
        return True
    return False


# text = 'You can call me at +55 48 3322 0124 or 005548 996153258'
# phones = extract_phone(text)
# print(phones)
# for phone in phones:
#     for i in range(1):
#         if is_valid_phone(phone[i]):
#             print(f'{phone[i]} - This is a real phone number')


print(is_valid_phone('0055 (48) 99615 3258'))
print(is_valid_phone('mhiloca@gmail.com'))
print(is_valid_phone('48 996153258wee'))
