# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.







# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# choosing a random number between 1 and 100
import random

EASY_ATTEMPT = 10
HARD_ATTEMPT = 5

def generated_number():

    return random.randint(1,100)
# Make function to choose difficulty and set attempts

def game_level():
    difficulty_level = input(" Please select a game level 'easy' or 'hard' to play ")
    if difficulty_level == "easy":
        return EASY_ATTEMPT
    elif difficulty_level == "hard":
        return HARD_ATTEMPT
    else:
        print("wrong game level option selected ")
        return None


# Let the user guess a number

def guess_number():
    chosen_number = 0
    chosen_number = int(input("guess a number between 1 and 100 "))
    while chosen_number not in range(1,101):

        print(f"bad number selected : {chosen_number}")
        chosen_number = input("guess a number between 1 and 100 ")
    return chosen_number


# Function to check user guess against actual answer

def validate_number(userNumber, computerNumber, attempts_left):
    if userNumber > computerNumber:
        print("number guessed is too high ")
        attempts_left -= 1
    elif userNumber < computerNumber:
        print("number guessed is too low ")
        attempts_left -= 1
    else:
        print("Hurray you guessed it correct ")
        attempts_left = None

    return attempts_left

# Track the number of turns and reduce the number by 1 if the user got it wrong

# repeat the guessing functionality if user got it wrong

# if they get it right say you got it right

# prompt to play again

# Press the green button in the gutter to run the script.

def play_game():

    number_of_attempts = game_level()
    print(f"you have {number_of_attempts} left to correctly guess ")
    generate_number = generated_number()

    user_number = guess_number()

    while number_of_attempts !=0:
        number_of_attempts = validate_number(user_number, generate_number, number_of_attempts)
        print(f"you have {number_of_attempts} attempts left to correctly guess ")
        if number_of_attempts is None:
            break
        user_number = guess_number()


    if number_of_attempts == 0:
        print("Game over!!!! no more attempts left")

if __name__ == '__main__':
    quit_game = False
    while quit_game != True:
        game_choice = input("do you want to play guess the number game ? Select 'y' or 'n' ")
        if game_choice == 'y':
            play_game()
        else:
            quit_game = True





