import re


def parse_phone1(s):
    pattern = '''
                \s*
                \((?P<area_code>\d{3})\)
                \s*
                (?P<first_three>\d{3})
                 -
                (?P<last_four>\d{4})
                           
                 '''
    matcher = re.compile(pattern, re.VERBOSE)
    matches = matcher.match(s)
    if matches:
        return (matches.group('area_code'), matches.group('first_three'), matches.group('last_four'))
    raise ValueError("invalid phone number")
