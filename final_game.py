# Paul McJannet | Student no. 41171723 | Python Game
# TODO: add timer, results, leaderboard, sign in/up...

# import modules
import random
from sys import exit

# text output explaining how the game works
print("\n***** Hello, and Welcome to the Number Guessing Game!*****\n\n~~~Rules~~~\n-- You need to correctly guess a random number.\n-- This starts by selecting your level (1, 2 or 3) which will change the range of possible numbers to guess from.\n-- After each guess, you will be told if the random number is higher or lower than your most recent guess.\n\n~~~Options~~~\nAt any time:\n-- Type 'q' then 'ENTER' to quit the program\n\n~~~Levels~~~\n-- Type '1' to guess from 1 - 10\n-- Type '2' to guess from 1 - 100\n-- Type '3' to guess from 1 - 1000")

 # text output explaining how the game works
    # print("\n***** Hello, and Welcome to the Number Guessing Game!*****\n\n~~~Rules~~~\n-- You need to correctly guess a random number.\n-- This starts by selecting your level (1, 2 or 3) which will change the range of possible numbers to guess from.\n-- After each guess, you will be told if the random number is higher or lower than your most recent guess.\n-- Once you guess correctly, the game timer will end.\n-- If you beat either a high score (least guesses needed to guess correct) or the timer (fastest time to guess correct) you might just get lucky enough to add your name to the Top 10 Leaderboard!\n\n~~~Options~~~\nAt any time:\n-- Type 'q' then 'ENTER' to quit the program\n-- Type 'leaderboard' then 'ENTER' to see all high scores and fastest times (note: this will not stop the timer if already in a game)\n\n~~~Level Selection~~~\nTo being, please select a level:\n-- Type '1' to guess from 1 - 10\n-- Type '2' to guess from 1 - 100\n-- Type '3' to guess from 1 - 1000")

# global variable needed to set range of numbers (depending on level selection, this is used inside functions with different scope)
set_upper_range = 0

# checks for user guess and responds if its higher, lower or correct while also validating if its an integer or a string
def main_game_loop(range):
    # generate the upper range number based on level selection 
    rand_number = random.randint(1, range)

    while True:
        prompt_guess = input(f"Guess a number between 1 - {range}: ")

        # see if input can be converted into an integer
        try:
            convert_guess = int(prompt_guess)

            # if user guess is an integer and in the correct range (dictated by level selection)
            if convert_guess <= range and convert_guess > 0:
                if convert_guess == rand_number:
                    print(f"\n************************************************************************\nCongratulations! Your guess is correct and the number was {rand_number}!\n************************************************************************")
                     # TODO: if top 10 met in time or number of guesses ask for username (which eventually says thanks for playing and quits program)
                        # TODO: otherwise, say thanks for playing and quit program
                    break
                elif rand_number > convert_guess:
                    print(f"The number is greater than {convert_guess}, try again.\n")
                    continue
                elif rand_number < convert_guess:
                    print(f"The number is less than {convert_guess}, try again.\n")
                    continue

            # number is not in range, try again
            else:
                print(f"Number is not in range 1 - {range}, try again.\n")
                continue

        # anything except an integer is not valid input
        except:

            # user wants to quit program
            if prompt_guess == "q":
                print(f"\nThank-you for playing! See you next time!")
                exit()    
            
            # not valid input
            else:
                print(f"Not a valid number, try again.\n")
                continue

# level selection
def prompt_level_selection_fn():
    # need to access global variable
    global set_upper_range 
    
    while True:
        prompt_level = input("\nSelect a level, then 'ENTER': ")
        
        # valid choices
        if prompt_level == "1":
            set_upper_range = 10
            break
        elif prompt_level == "2":
            set_upper_range = 100
            break
        elif prompt_level == "3":
            set_upper_range = 1000
            break

        # user wants to quit program
            # TODO: stop timer and quit everything
        elif prompt_level == "q":
            print(f"\nThank-you for playing! See you next time!")
            exit()    
            #   elif:
            # # TODO: show leaderboard
            # print("show leaderboard....")
            # return False
        
        # not valid input
        else:
            print(f"Not a valid level selection, try again.\n")
            continue

if __name__ == "__main__":
    # begin level selection process
    prompt_level_selection_fn()

    # dictionary to help define level range chosen (helps with out message to user)
    level_match_value = {10: 1, 100: 2, 1000:3}

    # start game
    print(f"\nYou have selected level {level_match_value[set_upper_range]}.\n")
    main_game_loop(set_upper_range)



    # TODO: use secrets module?
        # TODO: use React for front end
        # TODO: function to show leaderboard, enter username, add to database!!
        # TODO: add AI model like tensorflow to predict average times, show data visualization of completionists, etc, etc. 
        # TODO: use python web services
        # TODO: status function that shows current number of guesses and the current range of numbers 
        # TODO: count how many guesses it took
        # TODO: add color to the terminal, and fix its rows and columns
        # https://pypi.org/project/tabulate/
        # https://github.com/Textualize/rich?tab=readme-ov-file

        # TODO: add timer
        # TODO: save data for leaderboard to a database?
        # TODO: modularize code?
        # .format() method on strings to make pretty with curly braces {} {} {}