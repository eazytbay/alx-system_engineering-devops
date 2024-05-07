
#!/usr/bin/python3
"""
A script that queries the Reddit API and returns the
number of subscribers for a given subreddit.
"""


import json
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    output = response.json()
    return output.get("data").get("subscribers")
