import tweepy
from random import randint
from time import sleep

CONSUMER_KEY = 'YlNgSe3AfQN7OieNLDETrXlEu'
CONSUMER_SECRET = 'wSZ2HGfRUsnvP36Wl8SjjsKrrOCQXuKfKOS1EvXZnPlfnHsOxw'
ACCESS_TOKEN = '1071076029702250497-LkFZDON35CCeXJywwtFVwnQEYLclqB'
ACCESS_TOKEN_SECRET = 'awVTO2pZuebhIVK1ErLDm3ZGDjP8uLofvm7cIgmmtbHOd'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

num=0
count=0
temp=0

while (count < 100):

    firstTweet = api.search("pd")[0]
    if firstTweet.id==temp:
        sleep(randint(10,20))
        continue

    rid=firstTweet.id
    rsn=firstTweet.user.screen_name

    m="@%s no, U" % (rsn)
    api.update_status(status=m, in_reply_to_status_id=rid)
    count=count+1
    print(count)
    temp = firstTweet.id
