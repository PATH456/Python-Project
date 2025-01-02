word_list = ["aardvark", "baboon", "camel"]


import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
stage_number = 6
chosen_word = random.choice(word_list)
process = list("_" * len(chosen_word))
correct_letter = []
for letter in range(len(chosen_word)):
    print("_", end = " ")
life_count = 7
while life_count > 0 and "".join(process) != chosen_word:
    user_guess = input("\nPick a letter to guess: ").lower()
    if user_guess in correct_letter:
        print("You have already guessed this letter")
    elif user_guess not in chosen_word:
        life_count -= 1
        print(f"Incorrect, you have {life_count} opportunities left")
        print(stages[stage_number])
        stage_number -= 1
    else:
        print("Correct")
        correct_letter.append(user_guess)
        for i in range(len(chosen_word)):
            if user_guess == chosen_word[i]:
                process[i] = user_guess
        print(" ".join(process))


if "".join(process) == chosen_word:
    print("Game over! You winnnnnnnnnnnnnnn <3")
elif life_count == 0:
    print("Game over! You loseeeeeee, hehe")



