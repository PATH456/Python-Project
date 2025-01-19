print("""This program is called Black Jack Game. Initially, you will get 2 random numbers as 2 cards, as long as the total
of them is less than 21, you can choose to get one more card or stop. You only know the first card of the computer.
There are 3 possible scenarios:
- Your total and computer's total are less than 22, depends on the computer's total, you could lose or win
- Your total is greater than 21 => You lose
- Your total is equal to computer's total or both the total is greater than 21 => Draw
""")

import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
list_number = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
your_card = []
computer_card = []
win = False
start_game = input("""Do you wanna play BlackJack Game?
Type 'y' for Yes and type 'n' for No
""")
if start_game == "y":
    print(logo)

for i in range(2):
    your_card.append(random.choice(list_number))
    computer_card.append(random.choice(list_number))
current_score = sum(your_card)
computer_score = sum(computer_card)
while computer_score <= 16:
    computer_card.append(random.choice(list_number))
    computer_score = sum(computer_card)

print(f"Your cards: {your_card}, current score {current_score}")
print(f"Computer cards: {computer_card[0]}")
while True:
    user_choice = input("Type 'y' to get another card, type 'n' to stop ")
    if user_choice == "y":
        your_card.append(random.choice(list_number))
        current_score = sum(your_card)
        print(f"Your cards: {your_card}, current score {current_score}")
        if len(your_card) == 5 and current_score <=21:
            print("You win!")
            win = True
            break
        elif current_score >= 21:
            break
    if user_choice == "n":
        break
print(f"Your cards: {your_card}, your final score is {current_score}")


if current_score < 22 and computer_score < 22 and win == False:
    if current_score > computer_score:
        print(f"Computer cards: {computer_card}, computer score is {computer_score}")
        print("You win!")

    elif current_score < computer_score:
        print(f"Computer cards: {computer_card}, computer score is {computer_score}")
        print("You lose!")

    elif current_score == computer_score:
        print(f"Computer cards: {computer_card}, computer score is {computer_score}")
        print("Draw!")

elif current_score > 21 and computer_score <= 21:
    print(f"Computer cards: {computer_card}, computer score is {computer_score}")
    print("You lose!")
elif current_score <= 21 and computer_score > 21:
    print(f"Computer cards: {computer_card}, computer score is {computer_score}")
    print("You win!")
elif computer_score > 21 and current_score > 21:
    print(f"Computer cards: {computer_card}, computer score is {computer_score}")
    print("Both lose!")

















