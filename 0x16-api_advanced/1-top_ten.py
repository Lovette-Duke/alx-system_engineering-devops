#!/usr/bin/python3
"""
use the Reddit API to scrape and prints the titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints titles.
    """
    result = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if result.status_code == 200:
        for get_data in result.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
