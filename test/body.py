import tweepy
import logging
import time
import random
from datetime import datetime, timedelta
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from config import create_api
api = create_api()


def check_for_followers(api,recent_following_user1,user_1,recent_following_user2,user_2,recent_following_user3,user_3,recent_following_user4,user_4,recent_following_user5,user_5):

    while True:


        time.sleep(23)

        for user in tweepy.Cursor(api.friends, screen_name=user_1).items(1):
            print("checking for new followings of "+user_1)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user1):
                recent_following_user1.append(latest_following)
                print(latest_following + " is followed by " + user_1)
                message=user_1+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1691472368:AAGOOBgFwZHzF5EWod7FD_zt6oLKjGaxf8E/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)

        time.sleep(18)


        for user in tweepy.Cursor(api.friends, screen_name=user_2).items(1):
            print("checking for new followings of "+user_2)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user2):
                recent_following_user2.append(latest_following)
                print(latest_following+" is followed by " + user_2)
                message=user_2+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1691472368:AAGOOBgFwZHzF5EWod7FD_zt6oLKjGaxf8E/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)
        time.sleep(15)

        for user in tweepy.Cursor(api.friends, screen_name=user_3).items(1):
            print("checking for new followings of "+user_3)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user3):
                recent_following_user3.append(latest_following)
                print(latest_following)
                message=user_3+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1691472368:AAGOOBgFwZHzF5EWod7FD_zt6oLKjGaxf8E/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)
        time.sleep(15)

        for user in tweepy.Cursor(api.friends, screen_name=user_4).items(1):
            print("checking for new followings of "+user_4)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user4):
                recent_following_user4.append(latest_following)
                print(latest_following)
                message=user_4+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1691472368:AAGOOBgFwZHzF5EWod7FD_zt6oLKjGaxf8E/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)
        time.sleep(15)

        for user in tweepy.Cursor(api.friends, screen_name=user_5).items(1):
            print("checking for new followings of "+user_5)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user5):
                recent_following_user5.append(latest_following)
                print(latest_following)
                message=user_5+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1691472368:AAGOOBgFwZHzF5EWod7FD_zt6oLKjGaxf8E/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)

        time.sleep(20*60)
            
    

#initial adding of followers to the array

recent_following_user1=[]
user_1="fomosaurus"
for user in tweepy.Cursor(api.friends, screen_name=user_1).items(10):
    new_follower=str(user.screen_name)
    recent_following_user1.append(new_follower)

time.sleep(120)

recent_following_user2=[]
user_2="CryptoSpider1"
for user in tweepy.Cursor(api.friends, screen_name=user_2).items(10):
    new_follower=str(user.screen_name)
    recent_following_user2.append(new_follower)


time.sleep(120)

recent_following_user3=[]
user_3="Privatechad_"
for user in tweepy.Cursor(api.friends, screen_name=user_3).items(10):
    new_follower=str(user.screen_name)
    recent_following_user3.append(new_follower)


time.sleep(120)

recent_following_user4=[]
user_4="AlgodTrading"
for user in tweepy.Cursor(api.friends, screen_name=user_4).items(10):
    new_follower=str(user.screen_name)
    recent_following_user4.append(new_follower)

time.sleep(120)


recent_following_user5=[]
user_5="Wangarian1"
for user in tweepy.Cursor(api.friends, screen_name=user_5).items(10):
    new_follower=str(user.screen_name)
    recent_following_user5.append(new_follower)

time.sleep(120)


recent_following_user6=[]
user_6="RayJay888"
for user in tweepy.Cursor(api.friends, screen_name=user_5).items(10):
    new_follower=str(user.screen_name)
    recent_following_user5.append(new_follower)
    
time.sleep(120)

#calling main function

while True:
    print("collected initial datas")
    time.sleep(119)
    check_for_followers(api,recent_following_user1,user_1,recent_following_user2,user_2,recent_following_user3,user_3,recent_following_user4,user_4,recent_following_user5,user_5)
    time.sleep(10*5)
print('\n\n\n                   finished following all                           ')

