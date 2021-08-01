import random
import re

# Write your code here
print("H A N G M A N\n")

active = True

while active:
    select = input("Type \"play\" to play the game, \"exit\" to quit: ")
    
    if select == "play":
        choice_list = ['python', 'java', 'kotlin', 'javascript']
        choice = random.choice(choice_list)

        b = ("-" *(len(choice)))
        print(b)

        tries = 8
        user_list = []
        while tries != 0:
            user_text = input("Input a letter: ")
            
            if not (len(user_text) == 1):
                print("You should input a single letter")
                print()
                print(b)
                continue

            if (not user_text.isalpha()) or (not user_text.islower()):
                print("Please enter a lowercase English letter")
                print()
                print(b)
                continue

            if user_text in user_list:
                print("You've already guessed this letter")
                print()
                print(b)
                continue
            else:
                user_list.append(user_text)

                if user_text not in choice:
                    tries -= 1
                    print("That letter doesn't appear in the word")
                    if tries == 0:
                        print("You lost!")
                    else:
                        print()
                        print(b)
                else:
                    a = [m.start() for m in re.finditer(user_text, choice)]
                    for i in a:
                        b = b[:i] + user_text + b[i+1:]
                    print()
                    print(b)
                    
            if b == choice:
                print(f"You guessed the word {choice}!")
                print("You survived!")
                break
            else:
                continue
    elif select == "exit":
        active = False
    else:
        continue