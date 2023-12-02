#!/usr/bin/python3
""" Python script that takes your GitHub credentials
 and uses the GitHub API to display your id"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    r = requests.get("https://api.github.com/user",read:user,
     {"username": argv[1], "password": argv[2]})
    if r.status_code == 200:
        print("succed",r.headers.get("id"))