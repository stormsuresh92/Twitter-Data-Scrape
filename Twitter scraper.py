import snscrape.modules.twitter as sntwitter
import pandas as pd
from time import sleep
from tqdm import tqdm

twitter_data = []

username = input('Enter your twitter username: ')
number = int(input('How many tweets do want to scrape: '))


for i, tweet in tqdm(enumerate(sntwitter.TwitterSearchScraper('{}'.format(username)).get_items())):
	if i > number:
		break

	twitter_data.append([tweet.date, tweet.content, tweet.user.username, tweet.url])
	sleep(0.2)

df = pd.DataFrame(twitter_data, columns=['Date', 'Tweets', 'Username', 'Url'])
df.to_csv(f'{username}.csv', index=False)