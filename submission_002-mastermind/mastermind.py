import random


def run_game():
    """
    TODO: implement Mastermind code here
    """
    my_list_code = []
    
    while len(my_list_code) != 4:
        random_numbers = str(random.randint(1, 8))
        my_list_code.append(random_numbers)
            
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    
    won = False
    count_guesses = 12
    
    while count_guesses >= 0 and not won:

        get_user_input = input("Input 4 digit code: ")

        if (len(get_user_input) is not len(my_list_code)) or (not get_user_input.isdigit()):
            print("Please enter exactly 4 digits.")
            get_user_input = input("Input 4 digit code: ")
        elif ("9" in get_user_input) or ("0" in get_user_input):
            print("Please enter exactly 4 digits.")
            get_user_input = input("Input 4 digit code: ")
        
        correct_digit = 0
        correct_place = 0
        for a in range(len(my_list_code)):
            for b in range(len(get_user_input)):
                if (get_user_input[a] == my_list_code[b]) and (a != b):
                    correct_digit += 1
                if (get_user_input[a] == my_list_code[b]) and (a == b):
                    correct_place += 1
                continue
        
        print("Number of correct digits in correct place:    ", str(correct_place))
        print("Number of correct digits not in correct place:", str(correct_digit))
        
        if count_guesses == 0:
            print("The code was: ", "".join(my_list_code), sep="", end="\n")
            break
        if (my_list_code == get_user_input) or (correct_place == 4):
            print("Congratulations! You are a codebreaker!")
            print("The code was: ", "".join(my_list_code), sep="", end="\n")
            won = True
            break
        
        if count_guesses == 0:
            break
        count_guesses -= 1
        print("Turns left:", str(count_guesses))

if __name__ == "__main__":
    run_game()
