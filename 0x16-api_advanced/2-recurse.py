#!/usr/bin/python3
"""
use the Reddit API to scrape and return
a list of the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    use the reddit API and get
    a list containing the titles of all hot articles
    """
    result = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if result.status_code == 200:
        for get_data in result.json().get("data").get("children"):
            content = get_data.get("data")
            title = content.get("title")
            articles.append(title)
        after = result.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
