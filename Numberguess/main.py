import random

computer_choice = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I will think of a number between 1 and 100")
attemps = 0
while attemps==0:
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if user_choice == 'easy':
        attemps = 10
    elif user_choice == 'hard':
        attemps = 5
    else:
        print("Wrong choice")

while attemps>0:
    print(f"You have {attemps} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess:"))
    if user_guess == computer_choice:
        print(f"You have guessed it correct {computer_choice}")
        break
    elif user_guess> computer_choice:
        print("Too high.")
    elif user_guess<computer_choice:
        print("Too low.")
    else:
        print("Wrong choice")
    attemps-=1
print("You have run out of guesses,You lose.")