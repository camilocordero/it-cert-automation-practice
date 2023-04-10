#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z][a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number or a symbol
    if username[0] in ['.', '_', '!'] or username[0].isdigit():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # False
    


