'''
Simple class for users 
'''

class user:
    def __init__(self, username: str, reviews = {}):
        self.username = username
        self.reviews = reviews
    
    def update_username(self, new_name:str):
        self.username = new_name

    def add_review(self, review: dict):
        self.reviews.update(review)
    
    def get_reviews(self):
        return self.reviews
    
    def get_name(self):
        return self.username