#!/usr/bin/python3
"""Python script that sends a POST request and displays the body"""
import requests
from sys import argv


if __name__ == "__main__":
    fetch_html = requests.get(argv[1])
    status = fetch_html.status_code

    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(fetch_html.text)
