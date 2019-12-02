import re

bytes_pattern = re.compile(r'\b[0-1]{8}\b')


def parse_bytes(string):
    match = bytes_pattern.findall(string)
    return match


