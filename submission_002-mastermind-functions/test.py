import random

correct = False
turns = 0


def creating_a_code():
    '''
    This function creates and returns the code to break.
    '''
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    return code


def user_input():
    '''
    This function takes input from user and returns it.
    '''
    answer = input("Input 4 digit code: ")
    return answer

def compare_input_and_code(answer, code):
    '''
    1.This function compares input with the code generated.
    2.Also checks how correct the input is to the code.
    3.Decides if game is won or not
    '''
    global correct
    global turns
    correct_digits_and_position = 0
    correct_digits_only = 0

    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    turns += 1

    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
        print('The code was: '+str(code))
    else:
        print('Turns left: '+str(12 - turns))
    if turns == 12:
        print('The code was: '+str(code))


def run_game():
    '''
    1. This function resposible to keep game running until game is won or lost.
    2. Calls the other functions in order to run.
    '''
    global turns
    code = creating_a_code()
    #print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    while not correct and turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        compare_input_and_code(answer, code)
        

if __name__ == "__main__":
    #This is the main function where the run_game function is called to run the game.
    run_game()
