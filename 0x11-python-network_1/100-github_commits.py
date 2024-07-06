#!/usr/bin/python3
"""
Python script that takes a repository
name and an owner name,
and lists the 10 most recent commits
"""
import requests
import sys


if __name__ == "__main__":
    """the main proccess"""
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    resp = requests.get(url)
    try:
        data = resp.json()
        for i in range(10):
            print(data[i]['parents'][0]['sha'], end=": ")
            print(data[i]['commit']['author']['name'])
    except Exception as e:
        pass
