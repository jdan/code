#!/usr/bin/python

import twitter
import time

def main():
    API = twitter.Api()
    
    while 1:
        tweets = API.GetSearch('teh')
        for tweet in tweets:
            print '%s: %s' % (tweet.user.screen_name, tweet.text)
        time.sleep(60)

if __name__ == '__main__':
    main()