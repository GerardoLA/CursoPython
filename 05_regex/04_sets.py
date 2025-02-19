

import re

username = "rubi.us_69+"
pattern = r"[\w._%+-]+"

match = re.search(pattern, username)
if match: 
    print("El nombre de usuario es valido: ", match.group())
else:
    print("El nokmbre de usuario es válido")