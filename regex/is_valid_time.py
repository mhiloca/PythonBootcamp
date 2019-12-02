import re


def is_valid_time(time):
    time_pattern = re.compile(r'[0-1]?[0-9]:[0-5][0-9]')
    if time_pattern.fullmatch(time):
        return True
    return False


time = '19:59'
print(is_valid_time(time))
