#!/usr/bin/python3
"""
A script that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    res = requests.get(url, headers=headers).json()
    top_ten = res.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for top in top_ten:
        print(top.get('data').get('title'))
