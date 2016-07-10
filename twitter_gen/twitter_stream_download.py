import tweepy
import os
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import json

import db_migration
import psycopg2
import logging

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='')
    return parser


class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, conn, api):
        pass
        
    def on_data(self, data):
        try:
            #f.write(data['created_at'].encode('utf-8') + '\n' + data['text'].encode('utf-8') + ' \n \n')
            info = json.loads(data)
            t_created_at = json.dumps(info['created_at'], indent=4, encoding='utf-8')
            t_tweet = json.dumps(info['text'], indent=4, encoding='utf-8')
            
            # print(t_created_at)
            # print(t_tweet)
            # x = api.rate_limit_status()
            # print(json.dumps(x['resources']['application']['/application/rate_limit_status'],indent=4))
            # print("----------------------------------")
            
            self.save_tweet(info['text'], info['created_at'])
            return True
        except BaseException as e:
            print("Error on_data and saving tweet: %s" % str(e))
            logging.info("Error on_data and saving tweet: %s" % str(e))
            time.sleep(10)
        return True
    
    def save_tweet(self, tweet, created_at):
        try:
            cursor = conn.cursor()
            query_str =  "INSERT INTO tweets (tweet, created_at) VALUES (%s, %s);"
            cursor.execute(query_str, (tweet, created_at))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("Error when saving tweet to db: %s" % str(e))
            logging.info("Error when saving tweet to db: %s" % str(e))
            
    def on_error(self, status):
        if status_code == 420:
            # returning True in on_data disconnects the stream
            # wait for 16 minutes
            logging.info("On_Error: 420. Waiting for 16 minutes before doing anything else...")
            time.sleep(16*60)
            return True
        print(status)
        return True

def convert_valid(one_char):
    """Convert a character into '_' if invalid.

    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

if __name__ == '__main__':
    logging.basicConfig(filename='./log/twetter_gen.log',level=logging.INFO)
    parser = get_parser()
    args = parser.parse_args()
    
    # First create database:
    db_host = os.getenv('DB_HOST', "localhost")
    db_port = os.getenv('DB_PORT', "5432")
    db_user = os.getenv('DB_USER', "postgres")
    db_name = os.getenv('DB_NAME', "postgres")
    db_pass = os.getenv('DB_PASS', "password")
    db_migration.run_migrations(db_host, db_port, db_user, db_pass, db_name)
    
    consumer_key = os.getenv('TW_CONSUMER_KEY', "default_value")
    consumer_secret = os.getenv('TW_CONSUMER_SECRET', "default_value")
    access_token = os.getenv('TW_ACCESS_TOKEN', "default_value")
    access_secret = os.getenv('TW_ACCESS_SECRET', "default_value")
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    api = tweepy.API(auth)
    x = api.rate_limit_status()
    #print(json.dumps(x, indent=4))
    #print(json.dumps(x['resources']['statuses']['/statuses/home_timeline'],indent=4))
    
    print(json.dumps(x['resources']['application']['/application/rate_limit_status'],indent=4))
    
    # Getting database connection
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            host=db_host,
            port=db_port,
            password=db_pass)
            
    except Exception as e:
        print "I am unable to connect to the database"
        print str(e)
    
    query1 = os.getenv('TW_QUERY_1', 'tesla')
    query2 = os.getenv('TW_QUERY_2', 'TeslaMotors')
    twitter_stream = Stream(auth, MyListener(conn, api))
    twitter_stream.filter(languages=["en"], track=[query1, query2])
    logging.info('Service for getting tweets started...')
