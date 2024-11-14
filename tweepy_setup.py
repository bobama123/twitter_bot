import tweepy
from openAI_setup import generate_tweet
import os
from dotenv import load_dotenv

load_dotenv()

# api_key = "sQXmCG7uNnrw6tEWztOQvevzA"
# api_secret = "I1NpjqOJo2zT13asI9Jth6XZKARxWDvsf9HEOMW1p4FMf5XDVe"
# bearer_token = r"AAAAAAAAAAAAAAAAAAAAAGGmwwEAAAAAWPVL4RanbiXsaXVqmiQDZUhc82E%3DuUrYTaYSPz5kjIxcRVOuLj2lmHQmHiy9Ncwj1ViEePganUR0EK"
# access_token = "1856047851635138560-a7dWsBDtr3i8IMKovsiA3iapkBYMuF"
# access_token_secret = "t0kumY9ntXk0zZ5P1LXDQb6jbD8HgvHxfufZRkqAKD3TX"

client = tweepy.Client(
    os.getenv("tweepy_bearer_token"), 
    os.getenv("tweepy_api_key"), 
    os.getenv("tweepy_api_secret"), 
    os.getenv("tweepy_access_token"), 
    os.getenv("tweepy_access_token_secret")
    )

auth = tweepy.OAuth1UserHandler(
    os.getenv("tweepy_api_key"), 
    os.getenv("tweepy_api_secret"), 
    os.getenv("tweepy_access_token"), 
    os.getenv("tweepy_access_token_secret")
    )
api = tweepy.API(auth)


tweet = generate_tweet()
client.create_tweet(text=tweet)


#1. Create environment variables file
#2. Commit the first edition to github (WITHOUT SECRET KEYS)
#3. Look into streaming with a timer for how many tweets put out a day so it's free
#4. If all works, look into being able to reply to tweets on my own posts
