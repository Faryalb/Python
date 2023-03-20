class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
def display_info(self):
    print(f"Hello my name is {first_name}") #when a user inputs their information the code will print Hello my name is, followed by their first name
    print(f"My last name is {last_name}")
    print(f"My email is {email}")
    print(f"I am {age} year's old")
    print(f"I am {is_rewards_member} a rewards member")
    print(f" i have {gold_card_points} points")

def enroll(self):
    self.is_rewards_member = True #in the user class the initial statement is false, but now it will change to true 
    self.gold_card_points = 200 
display_info()


def spend_points(self, amount):
    self.gold_card_points = (200 - 50) #this will deduct 50 points from initial balance of 200 
    self.gold_card_points = (200 - 80) #this will deduct 80 points from initial balance of 200 
display_info(_)


user1.display_info()enroll