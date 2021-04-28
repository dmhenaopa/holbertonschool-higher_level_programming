#!/usr/bin/python3
def uppercase(str):
    for s in str:
        ascii_code = ord(s)
        if ascii_code >= 97 and ascii_code <= 122:
            new_ascii_code = ascii_code - 32
        else:
            new_ascii_code = ascii_code
        print("{}".format(chr(new_ascii_code)), end="")
    print()
