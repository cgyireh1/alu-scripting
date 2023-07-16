#!/usr/bin/python3
"""
defines recursive function to query the Reddit API
to parse title of all hot article and print sorted count
"""

import requests


def count_words(subreddit, word_list, after=None, count={}):
    """
    queries the Reddit API
    parses title of all hot articles
    prints sorted count of given keywords
    """
    if not word_list:
        return
    for word in word_list:
        word = word.lower()
        if word not in count.keys():
            count[word] = 0
    headers = {'User-Agent': 'Mozilla/5.0'}
    if after is not None:
        sub_url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    else:
        sub_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(sub_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    try:
        data = response.json().get('data')
    except:
        return
    children = data.get('children')
    for child in children:
        title = child.get('data').get('title').lower()
        title = title.split(' ')
        for word in word_list:
            word = word.lower()
            count[word] += title.count(word)
    after = data.get('after')
    if after is not None:
        count_words(subreddit, word_list, after, count)
    else:
        result = []
        for k in sorted(count.keys()):
            if count[k] != 0:
                result.append(f'{k}: {count[k]}')
        for k in sorted(result, key=lambda x: (-int(x.split(': ')[1]), x.split(': ')[0])):
            print(k)
