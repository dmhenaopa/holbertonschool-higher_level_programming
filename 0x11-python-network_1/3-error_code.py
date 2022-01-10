#!/usr/bin/python3
"""Python script that sends a request and display the body"""
import urllib
from urllib import request
from sys import argv

if __name__ == "__main__":
    request_url = request.Request(argv[1])
    try:
        with request.urlopen(request_url) as response:
            print(response.read().decode("utf-8"))

    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
