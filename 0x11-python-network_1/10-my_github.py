#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and password)
and uses the GitHub API to display your id.

- The first argument will be your username.
- The second argument will be your password (personal access token).
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    repos = requests.get(url, auth=(username, token))
    try:
        repos.raise_for_status()
        json_ = repos.json()
        print(json_.get("id"))
    except requests.exceptions.RequestException:
        print("None")
