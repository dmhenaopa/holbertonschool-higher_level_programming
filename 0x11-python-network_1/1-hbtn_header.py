#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
from urllib import request


with request.urlopen('https://intranet.hbtn.io/status') as response:
    print(response.info()["X-Request-Id"])
