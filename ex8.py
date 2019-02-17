#Εισαγωγή του tweepy
import tweepy

#Κλειδιά
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Ο χρήστης εισάγει το πρώτο account του twitter.
name1 = input ( 'Εισάγεται έναν χρήστη του Twitter:' )

user1 = api.get_user(name1)
tweets1 = api.user_timeline( screen_name="%s" %name1 , count=10 )
follower1 = user1.followers.count

print ("Οι followers του πρώτου χρήστη είναι:")
print (follower1)




#Ο χρήστης εισάγει το δεύτερο account του twitter.
name2 = input ( 'Εισάγεται έναν χρήστη του Twitter:' )

user2 = api.get_user(name2)
tweets2 = api.user_timeline( screen_name="%s" %name2 , count=10 )
follower2 = user2.followers.count

print ("Οι followers του δεύτερου χρήστη είναι:")
print (follower2)


#Έυρεση του πλήθους των λέξεων στα tweets των δύο χρηστών.
class UsersTweets():

    def tweets(self,tweets1):
        wordssum1 = 0
        for tweet in tweets1:
            wordssum1= len(tweet.text.split()) + wordssum1
        print ("Το πλήθος των λέξεων στα τελευταία 10 tweets του 1ου χρήστη είναι:")
        print (wordssum1)
        return (wordssum1)

    def tweets(self, tweets2):
        wordssum2 = 0
        for tweet in tweets2:
            wordssum2 = len(tweet.text.split()) + wordssum2
        print ("Το πλήθος των λέξεων στα τελευταία 10 tweets του 2ου χρήστη είναι:")
        print (wordssum2)
        return (wordssum2)

userstweets = UsersTweets()

sum1 = userstweets.tweets(tweets1)
sum2 = userstweets.tweets(tweets2)

product1 = sum1*follower1
product2 = sum2*follower2

if product1>product2:
    print("Ο πρώτος χρήστης έχει μεγάλυτερο γινόμενο(πλήθος λέξεων*followers) με:")
    print (product1)
elif product1<product2:
    print("Ο δεύτερος χρήστης έχει μεγάλυτερο γινόμενο(πλήθος λέξεων*followers) με:")
    print (product2)
else: print ("Οι δύο χρήστες έχουν ίσα γινόμενα.")




