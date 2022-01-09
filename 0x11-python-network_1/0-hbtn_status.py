#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
from urllib import request
from urllib.request import unquote

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        fetch_html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(fetch_html)))
        print("\t- content: {}".format(fetch_html))
        print("\t- utf8 content: {}".format(fetch_html.decode('utf8')))
