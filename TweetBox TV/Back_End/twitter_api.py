import csv
import tweepy
from tweepy import OAuthHandler
import config
import sys
import pandas as pd
import random

consumer_key = config.twitter['consumer_key']
consumer_secret = config.twitter['consumer_secret']
access_key = config.twitter['access_key']
access_secret = config.twitter['access_secret']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


index = int(sys.argv[1])

df = pd.read_csv('tv_shows.csv')

column_list = df["title"].tolist()
title = column_list[index]
file_name = column_list[index]+'.csv'
def generate_random_lat_long():
    lat = random.uniform(24.396308, 49.384358)
    long = random.uniform(-124.848974, -66.885444)
    return lat, long

def remove_spaces(string):
    return string.replace(" ", "")

csvFile = open(file_name, 'w', encoding='utf-8')

csvWriter = csv.writer(csvFile)

for i in [1]:
    print(title)
    query = remove_spaces(title)
    for tweet in tweepy.Cursor(api.search_tweets,q=query,count=100,lang="en").items(10000):
    #print(tweet.text)
        if tweet.text is not None:
            lat, lon = generate_random_lat_long()
            csvWriter.writerow([title,
                                tweet.created_at,
                                tweet.user.followers_count,
                                tweet.user.friends_count,
                                tweet.text, lat, lon])
