#!/usr/bin/python3
"""
   text_indentation module:

   This module contain a method (text_indentation())
   that prints a text with 2 new lines after each of
   these characters . ? and :
"""


def text_indentation(text):
    """
       Method to print 2 new lines after an special character

       Args:
            param1 (text): String with the text
    """
    string = ""

    if type(text) is not str:
        raise TypeError('text must be a string')

    for i in range(0, len(text)):
        if text[i] != " ":
            string = string + text[i]
            if (text[i - 1] == '.' and
                    text[i - 1] == '?' and
                    text[i - 1] == ':'):
                string = string + "\n\n"
                continue

        elif (text[i] == " " and
              text[i - 1] == '.' or
              text[i - 1] == '?' or
              text[i - 1] == ':'):
            string = string + "\n\n"
            continue

        elif (text[i] == " " and
              text[i - 1] != '.' or
              text[i - 1] != '?' or
              text[i - 1] != ':'):
            string = string + text[i]
            continue

    print("{}".format(string), end="")
