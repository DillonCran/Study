###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!


"""
outline and code below
"""

# game outline
# welcome/intro/rules
# generate random number list
# ask for input
# compare input to list
# return error depending on answer relation to list
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
# repeat until match (possible max tries before restart)
# end screen, ask for replay or quit



# Declarations
import random

score = 0

def generate_list():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def compare_lists(list1, list2):
    # list1 = current_list \ list2 = guess
    # list1 comes in as a list, while list2 comes in as a single int
    split_guess = [int(x) for x in str(list2)]
    # full match
    if split_guess == list1:
        print("You've guessed the number correctly!")
        return 1
    # partial match
    elif any(num in list1 for num in split_guess):
        if split_guess[0] == list1[0] or split_guess[1] == list1[1] or split_guess[2] == list1[2]:
            print("Match: You've guessed a correct number in the correct position")
            return 0
        else:
            print("Close: You've guessed a correct number but in the wrong position")
            return 0
    # no match
    else:
        print("Nope: You haven't guess any of the numbers correctly")
        return 0


# game logic
game_on = True

while game_on:
    # gane intro/rules
    print("Welcome to the game!")
    print("The rules of the game are simple: I will think of a 3 digit number (ex. 231) and you will try to guess it.")
    print("Based on your guesses I will give you different clues, so pay attention!")
    start_play = input("Would you like to start playing? (y/n)")
    if start_play.lower() == "y":
        print("Let's begin!")
        # generate random number list
        current_list = generate_list()
        # ask for input
        guess = int(input("Alright the number is set, What is your guess? "))
        print("Alright good guess! Let's see the results.")
        # compare input to list
        result = compare_lists(current_list, guess)
        # while guess != current_list:
        while result == 0:
            guess = int(input("What is your next guess? "))
            result = compare_lists(current_list, guess)
        # end game with correct answer
        if result == 1:
            score += 1
            print(f"Congrats! Your score is {score}")
            # ask for replay or quit
            play_again = input("Would you like to play again?")
            if play_again.lower() == "y":
                game_on = True
            else:
                game_on = False


        