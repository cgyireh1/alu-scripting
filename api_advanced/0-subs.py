#!/usr/bin/python3

"""
Defines a function that queries the Reddit API and returns the number of subscribers for a given subreddit. 
"""


def number_of_subscribers(subreddit):
    """
    queries the Reddit API
    returns the number of subscribers for a given reddit
    """
    import requests
    subreddit_URL = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    
    # Setting the user agent header to identify the client making the API request
subreddit_info = requests.get(subreddit_URL,
                                  headers={"user-agent": "user"},
                                  allow_redirects=False).json()
    if "data" not in subreddit_info:
        return 0
    subscribers = subreddit_info.get("data").get("subscribers")
    return subscribers
