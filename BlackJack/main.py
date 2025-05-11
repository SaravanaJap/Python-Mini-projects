import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards = random.sample(cards,k=2)
computer_cards = random.sample(cards,k=1)

# user_choice = input("Do you want to play a game of BlackJack?Type 'y' or 'n': ")

def computer_card_check(cards,user_sum):
    new_card = random.choice(cards)
    cards.append(new_card)
    if sum(cards)>user_sum:
        return sum(cards)
    elif sum(cards)==21:
        return 21
    elif sum(cards)>21:
        return sum(cards)
    else:
        return  computer_card_check(cards,user_sum)



another_card = 'y'
game_continue = 'y'


while game_continue == 'y':
    user_cards = random.sample(cards, k=2)
    computer_cards = random.sample(cards, k=1)
    print(f"Your cards:{user_cards},current score: {sum(user_cards)}")
    print(f"Computer's first card:{computer_cards[0]}")
    if sum(user_cards)==21:
        print(f"Your final hand:{user_cards},final score: {sum(user_cards)}")
        print(f"Computer's final card:{computer_cards[0]}")
        break
    while another_card == 'y':
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == 'y':
            user_cards.append(random.choice(cards))
            print(f"Your cards:{user_cards},current score: {sum(user_cards)}")
            print(f"Computer's first card:{computer_cards[0]}")
        elif another_card == 'n':
            user_sum = sum(user_cards)
            computer_sum = computer_card_check(computer_cards,user_sum)
            if computer_sum == 21:
                print("its black jack")
            elif computer_sum>user_sum:
                print("user won")
            elif user_sum<computer_sum:
                print('computer won')
            print(computer_cards)
            break
        if sum(user_cards) == 21:
            print(f"Your final hand:{user_cards},final score: {sum(user_cards)}")
            print(f"Computer's final card:{computer_cards[0]}")
            break
        if sum(user_cards) > 21:
            print(f"Your final hand:{user_cards},final score: {sum(user_cards)}")
            print(f"Computer's final card:{computer_cards[0]}")
            break



    game_continue = input("Do you want to play a game of BlackJack?Type 'y' or 'n'")


print(user_cards)