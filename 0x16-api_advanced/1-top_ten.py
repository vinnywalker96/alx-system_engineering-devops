#!/usr/bin/python3
"""Import Libraries"""
import requests


def top_ten(subreddit):
    # Make a GET request to the Reddit API
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json", headers={"User-Agent": "Mozilla/5.0"})

    # Check if the response is valid
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()

        # Iterate over the first 10 posts
        for i in range(10):
            # Extract the title of each post
            title = data['data']['children'][i]['data']['title']
            return title
    return 0
