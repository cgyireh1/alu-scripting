#!/usr/bin/python3
"""
Defines a function that queries the Reddit API
and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
        queries the Reddit API
        returns the number of subscribers for a given reddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get(url, headers=headers).json()
    subscribers = r.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
