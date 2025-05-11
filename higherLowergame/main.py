from data import data2
from  art import  ascii_art
import random
import os

a = random.choice(data2)
b = random.choice(data2)
while a == b:
    b = random.choice(data2)
print(ascii_art)
game_contiue = True
score = 0
while game_contiue:
    winner =  'a' if int(a['followers']) > int(b['followers']) else 'b'
    print(f"compare A:{a['name']} a {a['description']} brand ")
    print("VS")
    print(f"compare B:{b['name']} a {b['description']} brand ")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == winner:
        a = b
        b = random.choice(data2)
        while a == b:
            b = random.choice(data2)
        score+=1
        print(f"You are right,your score:{score}")
        os.system('cls')
    else:
        print(f"Sorry,that's wrong.Final score:{score}")
        game_contiue = False
