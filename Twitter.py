import snscrape.modules.twitter as sntwitter
import pandas as pd

username = input('Enter your Twitter username: ')
number = int(input('How many tweets do you want to scrape: '))

# Creating list to append tweet data to
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{}'.format(username)).get_items()):
    if i>number:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.url])
    
# Creating a dataframe from the tweets list above 
df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Tweets', 'Username', 'Url'])
df.to_csv(f'{username}.csv', index=False, encoding='utf-8')
