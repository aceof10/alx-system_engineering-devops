#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit. Returns None if no results are found
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Chrome/0.1'}
    params = {'limit': 100, 'after': after}

    try:
        res = requests.get(
                url, headers=headers, params=params, allow_redirects=False
        )
        if res.status_code == 200:
            data = res.json().get("data", {})
            posts = data.get("children", [])

            for post in posts:
                hot_list.append(post.get("data", {}).get("title", ""))

            after = data.get("after", None)
            if after is not None:
                return recurse(subreddit, hot_list, after)

            return hot_list if hot_list else None
        else:
            return None
    except requests.RequestException:
        return None
