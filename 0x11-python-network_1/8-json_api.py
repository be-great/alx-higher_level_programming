#!/usr/bin/python3
"""
Python script that takes
in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
