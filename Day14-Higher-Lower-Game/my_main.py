####.......This code is written by @ShoaibIqbalKhan.......####

from random import randint
# import random
from art import logo, vs
from game_data import data
import os
clear = lambda: os.system('cls')

score = 0
clear()
print(logo)
status = True
B = randint(0, len(data) - 1) #Account B
# B = random.choice(data)

while status:
    A = B  #Previous Account B assigned to Account A
    B = randint(0, len(data) - 1) #New Account A
    # B = random.choice(data)
    while A == B:
        B = randint(0, len(data) - 1)
        # B = random.choice(data)

    print(f"Compare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}")
    print(vs)
    print(f"with B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}")

    choice = input("Who has more followers 'A' or 'B': ").lower()
    if choice == 'a':
        # 'a' and 'b' are used as arguments
        a = A 
        b = B
    else: 
        b = A
        a = B

    clear()
    print(logo)
    
    def compare(a, b):
        """Compare account 'A' and account 'B' and give feedback to user"""
        if data[a]['follower_count'] > data[b]['follower_count']:
            global score 
            score += 1
            print(f"You're right! Current score {score}")
        else:
            global status
            status = False
            print(f"Sorry! You're wrong. Final score {score}")
            print("Game Over!")
            
    compare(a = a, b = b)
