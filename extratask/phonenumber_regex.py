import re
def parse_phone2(s):
    pattern = '''
        ^\s* # Leading spaces
       (?P<area_code>
        \d{3}-? # "xxx" or "xxx-"
       | \(\d{3}\)\s* # OR "(xxx) "
        )
      (?P<prefix>\d{3}) # xxx
       -? # Dash (optional)
      (?P<suffix>\d{4}) # xxxx
     \s*$ # Trailing spaces
     '''


    matcher = re.compile(pattern, re.VERBOSE)
    matches = matcher.match(s)
    if matches is None:
        raise ValueError("'{}' is not in the right format.".format(s))
    area_code = re.search('\d{3}', matches.group('area_code')).group()
    prefix = matches.group('prefix')
    suffix = matches.group('suffix')
    return (area_code, prefix, suffix)



s="  (404)   555-1212  "

print(parse_phone2(s))
# pass_phone2("(404)555-1212  ", '404', '555', '1212')
# pass_phone2("  404-555-1212 ", '404', '555', '1212')
# pass_phone2("  404-5551212 ", '404', '555', '1212')
# pass_phone2(" 4045551212", '404', '555', '1212')

