import random
from game_data import data
from art import logo,vs
from replit import clear

def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess,a_follower_count ,b_follower_count):
    if a_follower_count>a_follower_count:
        return guess=="a"
    else:
        return guess=="b"




score=0



account_B= random.choice(data)

flag =True
while flag:
    account_A= account_B
    account_B= random.choice(data)

    while account_A==account_B:
        account_B= random.choice(data)

    print(logo)
    
    print(f"Compare A: {format_data(account_A)}")
    
    print(vs)
    
    print(f"Compare B: {format_data(account_B)}")
    
    guess = input("Who has more follwers? Type 'A' or 'B': ").lower()
    
    a_follower_count = int( account_A["follower_count"])
    b_follower_count = int( account_B["follower_count"])
    
    
    is_correct = check_answer(guess,a_follower_count ,b_follower_count)
    clear()   
    
    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}.")
        
    else: 
        print(f"Sorry, that's wrong. Final score: {score}")
        flag = False