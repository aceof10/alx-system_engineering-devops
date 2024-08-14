#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)
"""
from collections import Counter
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    recursively queries the Reddit API,
    counts and prints sorted keyword occurrences
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    try:
        res = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if res.status_code == 200:
            data = res.json().get("data", {})
            posts = data.get("children", [])
            after = data.get("after", None)

            for post in posts:
                hot_list.append(post.get("data", {}).get("title", "").lower())

            if after is not None:
                return count_words(subreddit, word_list, hot_list, after)

            word_count = Counter()

            for title in hot_list:
                words = title.split()
                for word in word_list:
                    word_count[word.lower()] += words.count(word.lower())

            word_count = {
                word: count for word,
                count in word_count.items() if count > 0
            }

            sorted_word_count = sorted(
                word_count.items(),
                key=lambda item: (-item[1], item[0])
            )

            for word, count in sorted_word_count:
                print(f"{word}: {count}")
        else:
            return None
    except requests.RequestException:
        return None
