import re

def isValid(pascal_identifier: str):
    if len(pascal_identifier) > 6:
        return False
    if len(pascal_identifier) < 1:
        return False
    if re.match('^[a-zA-z][a-zA-z0-9]*$', pascal_identifier):
        return True
    return False