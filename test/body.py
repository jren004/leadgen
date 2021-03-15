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


def check_for_followers(api,recent_following_user1,user_1,recent_following_user2,user_2,recent_following_user3,user_3,recent_following_user4,user_4,recent_following_user5,user_5,recent_following_user6,user_6,recent_following_user7,user_7,recent_following_user8,user_8,recent_following_user9,user_9,recent_following_user10,user_10):

    while True:

        time.sleep(30)

        for user in tweepy.Cursor(api.friends, screen_name=user_1).items(4):
            print("checking for new followings of "+user_1)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user1):
                recent_following_user1.append(latest_following)
                print(latest_following + " is followed by " + user_1)
                message=user_1+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1691472368:AAGOOBgFwZHzF5EWod7FD_zt6oLKjGaxf8E/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)

        time.sleep(15)


        for user in tweepy.Cursor(api.friends, screen_name=user_2).items(4):
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

        for user in tweepy.Cursor(api.friends, screen_name=user_3).items(4):
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

        for user in tweepy.Cursor(api.friends, screen_name=user_4).items(4):
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

        for user in tweepy.Cursor(api.friends, screen_name=user_5).items(4):
            print("checking for new followings of "+user_5)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user5):
                recent_following_user5.append(latest_following)
                print(latest_following)
                message=user_5+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1691472368:AAGOOBgFwZHzF5EWod7FD_zt6oLKjGaxf8E/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(25)
        time.sleep(2)


        for user in tweepy.Cursor(api.friends, screen_name=user_6).items(4):
            print("checking for new followings of "+user_6)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user6):
                recent_following_user6.append(latest_following)
                print(latest_following + " is followed by " + user_6)
                message=user_6+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1618321351:AAFlOSvsR_sBwR82yB-hNXdRQeET-XzGxeg/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)
        time.sleep(15)

        for user in tweepy.Cursor(api.friends, screen_name=user_7).items(4):
            print("checking for new followings of "+user_7)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user7):
                recent_following_user7.append(latest_following)
                print(latest_following + " is followed by " + user_7)
                message=user_7+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1618321351:AAFlOSvsR_sBwR82yB-hNXdRQeET-XzGxeg/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)
        time.sleep(15)

        for user in tweepy.Cursor(api.friends, screen_name=user_8).items(4):
            print("checking for new followings of "+user_8)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user8):
                recent_following_user8.append(latest_following)
                print(latest_following + " is followed by " + user_8)
                message=user_8+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1618321351:AAFlOSvsR_sBwR82yB-hNXdRQeET-XzGxeg/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)

        time.sleep(15)

        for user in tweepy.Cursor(api.friends, screen_name=user_9).items(4):
            print("checking for new followings of "+user_9)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user9):
                recent_following_user9.append(latest_following)
                print(latest_following + " is followed by " + user_9)
                message=user_9+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1618321351:AAFlOSvsR_sBwR82yB-hNXdRQeET-XzGxeg/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)
        time.sleep(15)


        for user in tweepy.Cursor(api.friends, screen_name=user_10).items(4):
            print("checking for new followings of "+user_10)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user10):
                recent_following_user10.append(latest_following)
                print(latest_following + " is followed by " + user_10)
                message=user_10+" just followed " + latest_following +" \nClick on this link to view the profile : https://twitter.com/"+latest_following
                base_url='https://api.telegram.org/bot1618321351:AAFlOSvsR_sBwR82yB-hNXdRQeET-XzGxeg/sendMessage?chat_id=-1001441789928&text={}'.format(message)
                requests.get(base_url)
                time.sleep(5)
        time.sleep(15)


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
user_6="wojakchef"
for user in tweepy.Cursor(api.friends, screen_name=user_6).items(10):
    new_follower=str(user.screen_name)
    recent_following_user6.append(new_follower)


time.sleep(120)


recent_following_user7=[]
user_7="thegostep"
for user in tweepy.Cursor(api.friends, screen_name=user_7).items(10):
    new_follower=str(user.screen_name)
    recent_following_user7.append(new_follower)


time.sleep(120)


recent_following_user8=[]
user_8="Fiskantes"
for user in tweepy.Cursor(api.friends, screen_name=user_8).items(10):
    new_follower=str(user.screen_name)
    recent_following_user8.append(new_follower)


time.sleep(120)


recent_following_user9=[]
user_9="CryptoNekoZ"
for user in tweepy.Cursor(api.friends, screen_name=user_9).items(10):
    new_follower=str(user.screen_name)
    recent_following_user9.append(new_follower)


time.sleep(120)


recent_following_user10=[]
user_10="Darrenlautf"
for user in tweepy.Cursor(api.friends, screen_name=user_10).items(10):
    new_follower=str(user.screen_name)
    recent_following_user10.append(new_follower)
time.sleep(120)

#calling main function

while True:
    print("collected initial datas")
    time.sleep(119)
    check_for_followers(api,recent_following_user1,user_1,recent_following_user2,user_2,recent_following_user3,user_3,recent_following_user4,user_4,recent_following_user5,user_5,recent_following_user6,user_6,recent_following_user7,user_7,recent_following_user8,user_8,recent_following_user9,user_9,recent_following_user10,user_10)
    time.sleep(10*5)
print('\n\n\n                   finished checking  all                           ')

