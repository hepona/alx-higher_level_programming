#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
 and displays the value of the variable X-Request-Id """
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code == 200:
        print(res.headers["X-request-Id"])
