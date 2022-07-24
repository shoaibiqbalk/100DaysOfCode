import random
coin = ["heads", "tales"]
user_choice = input("Heads or Tales: ").lower()
toss = random.choice(coin)
if user_choice == toss:
    print(f"Toss Result is {toss}. You win")
else:
    print(f"Toss Result is {toss}. You loss")
