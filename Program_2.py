#Regular Expression Library
import re

#tweepy for accessing the twitter API
import tweepy

#To read and write tabular data in CSV format
import csv

#textblob library for processing textual data
from textblob import TextBlob

#Consumer and Access keys for twitter
ckey="f5L2tUzaG1XkE3v1yOS8q6Xgk"
csecret="0dGBCb1Rdnm9mhs5j2qmNLjbt5xxRbIy3TsFLIiad1AcHNghVr"
atoken="1044598050730258434-2cEtbBJrHSDtZxn0XEgD3zkSwdHySL"
asecret="VVV38Gl6nilc3YYj6m5ekBx6pFZjcUNtFxrgpf7NN7dYy"

#Authenticating access to twitter data
auth = tweepy.auth.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = tweepy.API(auth,wait_on_rate_limit=True)

# Appending twitter data to CSV file (create if file is not exist of same name)
csv_file = open('file.csv', 'w')
fieldnames=["Tweet","Score","Sentiment"]

#Use CSV Dict writer
csvWriter = csv.DictWriter(csv_file,fieldnames=fieldnames)
csvWriter.writeheader()
with open ("tweets.csv","r") as f_obj:
    fieldnames=["Tweet","Score","Sentiment"]

    #use CSV Dict reader
    reader=csv.DictReader(f_obj,fieldnames)
    for row in reader:
        dict_row=dict(row)
        print(dict_row)
        #updating tweet text by removing URLs and special characters to perform sentimental analysis
        updTweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str(dict_row)).split())

        #creating TextBlob object by passing updated tweet text
        analysis = TextBlob(updTweet)

        # set sentiment
        tweet_polarity = analysis.sentiment.polarity
        print(">>> Polarity score is %.2f" % tweet_polarity)

        #Stating tweet is positive, negative or neutral using polarity score
        if tweet_polarity > 0.0:
            tweet_sentiment = "Positive"
        elif tweet_polarity < 0.0:
            tweet_sentiment = "Negative"
        else:
            tweet_sentiment = "Neutral"

        print(">>> This tweet is %s" % tweet_sentiment)
        print("=================================================================================================\n")

        # Write a row to the CSV file using encode UTF-8
        csvWriter.writerow({"Tweet" : updTweet.encode('utf-8'),"Score":analysis.sentiment.polarity,"Sentiment" : tweet_sentiment})
