#tweepy for accessing the twitter API
import tweepy

#cvs library to support CSV files
import csv

#Consumer and Access keys for twitter
ckey="uZauPypsfMelDtpQrhT6VVfb1"
csecret="TeSu2BH2JHSiDMgmPA4qhwN9r2UgjLrU4XMgUU7C0Evg7DdhgJ"
atoken="1044599110471479296-CM9LqcDg2aeN1GFq30wQ4tjTQeA4ei"
asecret="nGvxjhrHlWkankSlShJH3uupVaSa0tR81ayZh7pij7mnb"

#Authenticating access to twitter data
auth = tweepy.auth.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = tweepy.API(auth,wait_on_rate_limit=True)

#Appending twitter data to CSV file (create if file is not exist of same name)
csv_file = open('tweets.csv', 'w')
csvWriter = csv.writer(csv_file)

#Asking for a user input to search keyword in tweets
keyword=input("Enter the tweet keyword :-")

#For loop to write csv file with tweeter dataset
for tweet in tweepy.Cursor(api.search,q = keyword, lang="en").items(limit=1001):

    csvWriter.writerow([tweet.text.encode('utf-8')])
    print(tweet.text)
csv_file.close()
