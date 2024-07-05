#!/usr/bin/python3
""" Python script that fetches a url"""
import urllib.request


if __name__ == "__main__":
    """What's my status? #0 """

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        status = response.status

    print("- type: {}".format(type(html)))
    print("- content: {}".format(html))
    print("- utf-8 content: {}".format(html.decode("utf-8")))
