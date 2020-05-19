"""Some functions to help the web app to make the viz.

We will do all the data manipulation here to compartmentalize
it from the app creation.
"""
from functools import reduce

import pandas as pd

from config import TWEETS_CSV


def get_hashtags(filepath=TWEETS_CSV):
    """Will procure a list of unique hashtags based
    from the tweets. Order by first letter after the #."""
    # Read the data from CSV
    df = pd.read_csv(filepath)

    # Get rows with hashtags only, lessen the processing time
    hashtags = df.hashtags[df.hashtags.notnull()]

    # Transform to lists 
    hashtags_list = [h.split(",") for h in hashtags]

    # Flatten the list of lists
    hashtags_flat = reduce(lambda x, y: x+y, hashtags_list)

    # Get unique values only
    hashtags_set = set(hashtags_flat)

    # Sort by alphabetical order
    return sorted(hashtags_set, key=str.lower)


def get_tweets_w_hashtag(hashtag, filepath=TWEETS_CSV):
    """Get the tweets with a particular hashtag"""
    # Read the data from CSV
    df = pd.read_csv(filepath)

    # Get tweets with hashtags
    df = df[df.hashtags.notnull()]
    return df[df["hashtags"].str.contains(hashtag)]
