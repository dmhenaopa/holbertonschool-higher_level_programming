#!/usr/bin/python3
def islower(c):
    ascii_code = ord(c)
    if ascii_code >= 97 and ascii_code <= 122:
        return True
    else:
        return False
