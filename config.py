"""Will contain the config variables for the app."""

import os

INPUT_CSV = os.getenv("INPUT_CSV", "data/tweets.csv")
OUTPUT_CSV = os.getenv("INPUT_CSV", "data/processed_tweets.csv")

TWEETS_CSV = os.getenv("TWEETS_DATA", "data/processed_tweets.csv")
