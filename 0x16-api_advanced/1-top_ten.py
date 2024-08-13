#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed
    for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Chrome/0.1'}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code == 200:
            data = res.json()
            posts = data.get("data", {}).get("children", [])

            if not posts:
                print(None)

            for post in posts:
                print(post.get("data", {}).get("title", ""))
        else:
            print(None)
    except requests.RequestException:
        print(None)
