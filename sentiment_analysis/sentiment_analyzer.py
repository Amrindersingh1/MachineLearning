import tweepy
from textblob import TextBlob

consumer_key = "KPk8LWSotf4yb6hecF7D4tYV2"
consumer_secret = "Zakm5HYZAKRTJQ7xQMWvz7G0d586lMViLRDtuzePqlqMyo2ubE"

access_token = "3393900808-U82f8wyzxqYGZkHvi6tjcNenKo6PeL57DJwBE3v"
access_token_secret = "pIQGctywwvFcdPowRXVMiVAIGdaHrhMsA0lFBkFWYZTHM"

try:
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	public_tweets = api.search('bangalore')

	for tweet in public_tweets:
		print(tweet.text)

		analysis = TextBlob(tweet.text)
		print(analysis.sentiment.polarity)

except Exception as e:
    print(e)