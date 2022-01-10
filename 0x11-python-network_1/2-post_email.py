#!/usr/bin/python3
"""Python script that sends a POST request with email as parameter"""
import urllib.parse
import urllib.request
from sys import argv

if __name__ == "__main__":
    values = {"email": argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    request = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
