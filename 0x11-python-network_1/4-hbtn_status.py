#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    if response.status_code == 200:
        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")
