# hellobot

import praw


# reddit api login
reddit = praw.Reddit(client_id='add id',
                     client_secret='add secret',
                     username='user',
                     password='pass',
                     user_agent='HelloBot ti saluta')
                    

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('testabot')

# words to activate the bot
saluti = ["Ciao","ciao","Salve","salve","Buongiorno","buongiorno"]

# look for words in the comment and reply appropriately
for comment in subreddit.stream.comments():
    if any(word in comment.body for word in saluti):

                reply = "Eccomi, sono un bot."
                comment.reply(reply)
                print('posted')
        
   
        
        
