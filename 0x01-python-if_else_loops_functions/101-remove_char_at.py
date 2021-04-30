#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    for s in str:
        if n > (len(str) - 1) or n < 0:
            return str

        else:
            if s == str[n]:
                continue

            else:
                new_string = new_string + s

    return new_string
