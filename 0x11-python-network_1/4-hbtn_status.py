#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    fetch_html = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("    - type: {}".format(type(fetch_html.text)))
    print("    - content: {}".format(fetch_html.text))
