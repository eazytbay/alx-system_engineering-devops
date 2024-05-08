#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/aaorrico23)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    results = response.json().get("data")
    return results.json().get("data").get("subscribers")
