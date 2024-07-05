#!/usr/bin/python3
"""
Python script that takes in a URL, sends
a request to the URL and displays the value
of the variable X-Request-Id in the
response header
"""
import requests 
import sys


if __name__ == "__main__":
    """ 5. Response header value #1 """
    url = 'https://alx-intranet.hbtn.io'
    response = requests.get(sys.argv[1])
    id = response.headers.get("X-Request-Id")
    print(id)
