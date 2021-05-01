import re

def isValid(pascal_identifier: str):
    if re.match('[a-zA-z][a-zA-z0-9]*', pascal_identifier):
        return True
    return False