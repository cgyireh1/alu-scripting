#!/usr/bin/python3
"""
Defines a function to query the Reddit API
Print titles of the first 10 hot posts.
"""


def top_ten(subreddit):
    """
    Queries the Reddit API, prints the titles
    of the first 10 hot posts for a subreddit.
    """
    import requests

    subreddit_URL = (
        'https://www.reddit.com/r/{}/hot.json?limit=10'
        .format(subreddit)
    )

    # Setting user agent header to identify the
    # client making the API request
    subreddit_info = requests.get(subreddit_URL,
                                  headers={"user-agent": "user"},
                                  allow_redirects=False).json()

    if "data" not in subreddit_info:
        print("None")
        return

    children = subreddit_info.get("data").get("children")

    for child in children:
        print(child.get("data").get("title"))
