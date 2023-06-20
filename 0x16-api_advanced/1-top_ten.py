#!/usr/bin/python3
"""Import Libraries"""
import requests
import sys


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed

    Args:
        subreddit (_type_): _description_
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        title_post = data['data']
        return title_post
    return 0
