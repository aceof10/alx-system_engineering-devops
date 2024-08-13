#!/usr/bin/python3
"""
queries the Reddit API and returns the number
of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code == 200:
            data = res.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
