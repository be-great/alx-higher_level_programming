#!/usr/bin/python3
""" Python script that fetches a url"""
import request


if __name__ == "__main__":
    """What's my status? #0 """
    url = 'https://alx-intranet.hbtn.io/status'
    response = request.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
