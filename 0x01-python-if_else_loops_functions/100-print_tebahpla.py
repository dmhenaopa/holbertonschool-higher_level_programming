#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 0:
        number = i
    elif i % 2 == 1:
        number = i - 32
    print("{}".format(chr(number)), end="")
