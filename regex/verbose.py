import re

email_pattern = re.compile(r"""
                            ^([-a-zA-Z0-9_.]+)      #  username
                            @                       #  single @
                            ([-0-9a-z._]+           #  domain   
                            \.                      #  single period
                            [a-z.]{2,6})$           #  domain
""", re.X | re.I)

email = 'Mhiloca@gmail.com'
match = email_pattern.search(email)
print(match.groups())

