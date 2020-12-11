
import random

correct = False
turns = 0
correct_digits_and_position = 0
correct_digits_only = 0

def creating_a_code():
    '''
    Generates 4 digit code in the range of 1 to 8.
    '''
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code

def user_input():
	#This function takes input from user and returns it.
    answer = input("Input 4 digit code: ")
    return answer

def compare_input_and_code(answer, code):
    '''
    1. Compares the input from user to the code generated.
    2. Checks how many digits are correct and those in the correct place.
    '''
    global correct_digits_and_position
    global correct_digits_only
    
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))


def is_game_won(correct_digits_and_position, turns):
    '''
    Checks if the game has been won or not won.
    '''
    global correct

    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))


def the_code_was(code):
    print('The code was: '+str(code))


def run_game():
    # 1. This function runs the game.
    # 2. Calls other functions for the game to function properly.
    # 3. Keeps game running until won or lost.

    global correct
    correct = False
    global turns
    global correct_digits_and_position
    global correct_digits_only
    
    code = creating_a_code()
    
    while not correct and turns < 12:
        answer = user_input()
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        compare_input_and_code(answer, code)
        turns +=1
        is_game_won(correct_digits_and_position, turns)
        correct_digits_and_position = 0
        correct_digits_only = 0
    
    the_code_was(code)


if __name__ == "__main__":
    '''
    The main function that calls the function of running the game.
    '''
    run_game()