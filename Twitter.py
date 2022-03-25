from Socialmedia import Socialmedia

class Twitter(Socialmedia):
    
    def __init__(self, name):
        super().__init__(name)
        self.Tweets = []
        
    def getTweets(self):
        for tweet in self.Tweets: 
            print("entered tweet:"+tweet)
    
    def createNewTweet(self):
        createTweet=True
        tweetinput = input("enter your new tweet: ")
        if len(tweetinput)<=280:
            self.Tweets.append(tweetinput)
        else:
            createTweet=False
        return createTweet  

tweet = Twitter(Twitter)
tweet.createNewTweet()
tweet.getTweets()
