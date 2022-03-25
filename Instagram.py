from Socialmedia import Socialmedia

class Instagram(Socialmedia):
       
    def __init__(self, name):
        super().__init__(name)
        self.posts = []
        
    def getPosts(self):
        for post in self.posts: 
            print("entered post:"+post)
        
    def publishNewPost(self):
        publish=True
        postinput = input("enter your new post: ")
        if len(postinput)<=2200:
            self.posts.append(postinput)
        else:
            publish=False
        return publish  

insta = Instagram(Instagram)
insta.publishNewPost()
insta.getPosts()
