import tweepy
from openAI_setup import generate_tweet
import os
from dotenv import load_dotenv
import time

load_dotenv()


client = tweepy.Client(
    os.getenv("tweepy_bearer_token"), 
    os.getenv("tweepy_api_key"), 
    os.getenv("tweepy_api_secret"), 
    os.getenv("tweepy_access_token"), 
    os.getenv("tweepy_access_token_secret")
    )


def tweet_creator():
    try:
        tweet = generate_tweet()
        print(f"Generated tweet: {tweet}")

        response = client.create_tweet(text=tweet)
        print("Tweet posted:", response)
        
    except Exception as e:
        print("Error while tweeting:", e)

if __name__ == "__main__":
    while True:
        tweet_creator()
        time.sleep(3600)


#1. Look into generating not duplicate tweets on your page
#2. If all works, look into being able to reply to tweets on my own posts
