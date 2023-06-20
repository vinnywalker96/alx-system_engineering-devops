#!/usr/bin/python3
""" Import Libraies"""
import requests


def number_of_subscribers(subreddit):
    """_queries the Reddit API and returns the number of subscribers

    Args:
        subreddit (string): _description_

    Returns:
        int: number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscibers = data['data']['subscribers']
        return subscibers
    return 0
