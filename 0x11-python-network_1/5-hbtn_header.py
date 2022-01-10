#!/usr/bin/python3
"""Python script that displays the value of variable X-Request-Id"""
import requests
from sys import argv


if __name__ == "__main__":
    fetch_html = requests.get(argv[1])
    print(fetch_html.headers['X-Request-Id'])
