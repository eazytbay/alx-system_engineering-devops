#!/usr/bin/python3
"""This is a function that prints hot posts on a given Reddit subreddit."""
import requests
def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for unexpected status codes
        results = response.json().get("data")
        if results:
            [print(c.get("data").get("title")) for c in results.get("children")]
        else:
            print("No posts found.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            print("Error: You may not have permission to access this subreddit.")
        else:
            print("HTTP Error:", e)
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

