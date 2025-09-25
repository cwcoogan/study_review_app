from review import Review
'''
'''

class Location:
    def __init__(self, name:str):
        self.name = name
        self.reviews = []
        #TODO could add a catagory for coffeeshop, classroom, outdoors, etc. 
    
    def add_review(self,new_review: Review):
        self.reviews.append(new_review)
