#!/usr/bin/python3
""" Python script that takes your GitHub credentials
 and uses the GitHub API to display your id"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    basic = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user",auth=basic)
    if r.status_code == 200:
        print("succed",r.headers.get("id"))