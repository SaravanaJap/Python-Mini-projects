import  random
from  words_list import word_list
from  ascii_art import  hang_man
print("Welcome to HangMan")

chosen_word = random.choice(word_list)
lives = 0
chosen_list = list(chosen_word)

blank_word = ""
for i in range(len(chosen_word)):
    blank_word+="_"
blank_list = list(blank_word)
while (lives<6) and  ('_' in blank_list):
    print("Word to find" +":"+ ''.join(blank_list))
    user_choice = input("Guess a letter : ").lower()
    for i in range(len(chosen_list)):
        if user_choice == chosen_list[i]:
            blank_list[i] = chosen_list[i]
            chosen_list[i] = "_"

            print(lives)
            break
        elif i == len(chosen_list)-1:
            lives+=1
            print(hang_man[lives])

    print(f"Lives left :{6-lives}")

