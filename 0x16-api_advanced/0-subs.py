
#!/usr/bin/python3
"""
A script that queries the Reddit API and returns the
number of subscribers
"""
def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
