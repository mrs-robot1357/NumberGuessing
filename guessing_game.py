import random

computer_guess = random.randint(1, 999)
# print(computer_guess)
user_score = 100
guess_count = 0
user_choice = int(input("Please enter any number of your choice: "))
while computer_guess != user_choice:
    if user_score <= 0:
        print(f"You have failed the game. Your score is 0%. The number was {computer_guess}.")
        print("Please play again, thanks!")
        break

    difference = user_choice - computer_guess
    c_difference = computer_guess - user_choice
    if user_choice > computer_guess:
        guess_count = guess_count + 1
        if difference >= 200:
            user_score = user_score - 10
            print("Much lower")
        elif difference >= 100 and (difference < 200):
            user_score = user_score - 7
            print("Still not there yet, go lower")
        elif difference >= 50 and (difference < 100):
            user_score = user_score - 3
            print("A little bit lower")
        elif difference >= 10 and (difference < 50):
            user_score = user_score - 2
            print("You're almost there, go slightly lower.")
        elif difference < 10:
            user_score = user_score - 1
            print("You're basically there. Just steps away. Try lower :)")
        else:
            break
    else:
        if c_difference >= 200:
            user_score = user_score - 10
            print("Much higher")
        elif c_difference >= 100 and (c_difference < 200):
            user_score = user_score - 7
            print("Still not there yet, go higher")
        elif c_difference >= 50 and (c_difference < 100):
            user_score = user_score - 3
            print("A little bit higher")
        elif c_difference >= 10 and (c_difference < 50):
            user_score = user_score - 2
            print("You're almost there, go slightly higher.")
        elif c_difference < 10:
            user_score = user_score - 1
            print("You're basically there. Just steps away. Try higher :)")
        else:
            break
    user_choice = int(input("Please guess again: "))
    continue

if computer_guess == user_choice:
    guess_count = guess_count + 1
    print(f"You got it! The number was {computer_guess}. It took you {guess_count} to get it correctly.")
    print(f"Your score is {user_score}%")









