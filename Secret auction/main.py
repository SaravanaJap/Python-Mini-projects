import os
from art import ascii
print(ascii)
print("Welcome to the secret auction program.")
detials = {}
bid_continue = "yes"
while bid_continue == 'yes':
    name  = input("What is your name?: ")
    bid_price = int(input("What's your bid?: "))
    detials[name] = bid_price
    bid_continue = input("Are there any othe bidders? Type 'yes' or 'no'.").lower()
    if bid_continue == 'yes':
        print('\n'*20)

winner = ''
amount = 0
for i in detials:
    if detials[i]>amount:
        amount = detials[i]
        winner = i

print(f"The winner is {winner} with a bid of ${amount}")


