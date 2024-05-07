#!/usr/bin/python3
"""
use the Reddit API to scrape the number of total subscribers on a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    queries a Reddit API for a subreddit.
    """
    result = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if result.status_code == 200:
        return result.json().get("data").get("subscribers")
    else:
        return 0
