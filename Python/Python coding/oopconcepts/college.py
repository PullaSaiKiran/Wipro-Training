
class College:
    def __init__(self , ccode ,cname , ccity):
        self.collegecode = ccode
        self.collegename = cname
        self.collcity = ccity

    def welcome_message(self):
        print("Hello there..!")

    def display_college_details(self):
        print(f'College code : {self.collegecode}\n college name : {self.collegename}\n city :{self.collcity}')

