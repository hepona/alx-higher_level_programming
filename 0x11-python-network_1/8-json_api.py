#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
 request to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    res = requests.post("http://0.0.0.0:5000/search_user", q)
    if isinstance(res.text, dict):
        print("Not a valid JSON")
    if len(res.text) == 0 or q == "":
        print("No result")
    else:
        print("[{}] {}".format(res.headers.get("id"), res.headers.get("name")))
    print(res.text)
