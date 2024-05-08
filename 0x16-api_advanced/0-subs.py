#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import json

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if an error occurs.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0 

    try:
        # Using format method for URL
        url = 'http://www.reddit.com/r/{}/{}.json'.format(subreddit, 'about')
        headers = {'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/aaorrico23)'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = json.loads(response.text)
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers

    except requests.exceptions.RequestException as e:
        print("Error retrieving subscriber count for '%s': %s" % (subreddit, e))
        return 0 
