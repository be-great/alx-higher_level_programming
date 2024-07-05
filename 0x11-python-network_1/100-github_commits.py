#!/usr/bin/python3
"""
Python script that takes a repository
name and an owner name,
and lists the 10 most recent commits
from the repository using the GitHub API.
Print all commits by: <sha>: <author name>
(one per line)
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url, params={'per_page': 10})

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    else:
        print("Failed to fetch commits")
