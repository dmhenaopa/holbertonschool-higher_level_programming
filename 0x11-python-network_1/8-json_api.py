#!/usr/bin/python3
"""Python script that sends a POST request with the letter as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        variable = ""
    else:
        variable = argv[1]
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': variable})

    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json["id"], json["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
