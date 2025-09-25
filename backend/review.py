'''
Review class for each review made on the application
'''


'''todo: how do I factor in the time stamp when creating a class like this?'''
class Review:
    def __init__(self, user: str, 
                 content: str, 
                 rating: int , 
                 location: str,
                 start_ts: str,
                 end_ts: str):
        self.username = user
        self.content = content
        self.rating = rating 
        self.location = location
        self.start = start_ts
        self.end_ts = end_ts
        self.total = end_ts- start_ts

    def edit_content(self,new_content: str):
        self.content = new_content