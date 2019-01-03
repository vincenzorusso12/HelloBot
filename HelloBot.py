# bigwordbot

import praw
import time

# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id='8Bm4CREcTjPKUg',
                     client_secret='nujVhfTAhyP8qd-Y5yXenW3n5t8',
                     username='momo584',
                     password='sticazzi',
                     user_agent='HelloBot ti saluta')
                    

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('testabot')

# phrase to activate the bot
saluti = ["Ciao","ciao","Salve","salve","Buongiorno","buongiorno"]

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if any(word in comment.body for word in saluti):

                reply = "Eccomi, sono un bot."
                comment.reply(reply)
                print('posted')
        
   
        
        
