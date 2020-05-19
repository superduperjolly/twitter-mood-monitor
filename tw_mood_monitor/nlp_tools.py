"""A module that contains the functions necessary for string manipulations for
the app."""

import pandas as pd


INPUT_CSV = "data/tweets.csv"
OUTPUT_CSV = "data/processed_tweets.csv"


def parse_hashtags(df):
    """Extracts the hashtags from the tweets.
    The output is an added column `hashtags` in
    the dataframe. All hashtags are in a list.

    Example:
    tweet: "#grandma is the #best"
    output: "#grandma,#best"
    """
    
    # Find all the hashtags in the tweet
    df["hashtags"] = df.text.apply(
        lambda tweet: ",".join([w for w in tweet.split() if w.startswith("#")])
    )

    return df


def normalize_time(df):
    """Extracts the HOUR of the time when the tweet
    was created."""
    
    # Extract the hour only
    df["created_at_hour"] = df.created_at.apply(
        lambda date: f"{date.hour}:00"
    )

    return df


def data_prep_pipeline(filepath, output_path):
    """Takes in a CSV with a specific format then runs
    a two-step data preparation to make the viz easier."""

    tweets_df = pd.read_csv(filepath, parse_dates=["created_at"])

    # Two step pipeline
    tweets_df = parse_hashtags(tweets_df)
    tweets_df = normalize_time(tweets_df)

    # Save to a CSV
    tweets_df.to_csv(output_path, index=False)

    return tweets_df


data_prep_pipeline(INPUT_CSV, OUTPUT_CSV)
print(f"Your processed tweets from {INPUT_CSV} are saved in {OUTPUT_CSV}")
