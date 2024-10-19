#3. Number Guessing Game
#Description: Create a game where the computer randomly selects a number, and the user has to guess it within a limited number of attempts. Provide hints for higher or lower.
#Skills Utilized: Random module, loops, conditionals, input/output.


import random
while True:
    numbers = range(1, 101)
    random_num = random.choice(numbers)
    count = 10
    while count > 0:
        user_guess = int(input("Guess a number from 1 to 100: "))
        if user_guess < 1 or user_guess > 100:
            print("Please guess a number within the range 1 to 100.")
        elif user_guess > random_num:
            count -= 1
            print(f"Too high! Try again! You have {count} chances left")
        elif user_guess < random_num:
            count -= 1
            print(f"Too low! Try again! You have {count} chances left")
        elif user_guess == random_num:
            print("Congratulations! You won")
            break
    if count == 0 and user_guess != random_num:
        print(f"You lose! The answer is {random_num}. Good luck next time")
    user_choice = input("Do you want to play again? (yes/no): ")
    if user_choice.lower() != "yes":
        break






