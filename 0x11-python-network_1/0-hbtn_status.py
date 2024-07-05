#!/usr/bin/python3
""" Python script that fetches a url"""
import urllib.request


if __name__ == "__main__":
    """What's my status? #0 """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        status = response.status
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode("utf-8")))
