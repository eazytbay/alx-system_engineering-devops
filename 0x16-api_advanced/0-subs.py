
#!/usr/bin/python3
"""
A script that queries the Reddit API and returns the
number of subscribers
"""
import requests
import sys

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data.get("data", {}).get("subscribers", 0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py subreddit_name")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

