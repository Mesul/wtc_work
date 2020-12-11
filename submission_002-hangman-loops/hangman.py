import random
import os




def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    
    while True:
        try:
            u_input = input('Guess the missing letter: ')
        except EOFError:
            break
        if u_input == "":
            get_user_input()
        else:
            return u_input
        break


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    
    status = '_'*len(word)
    status_list = list(status)
    lrandom_index = random.randint(0, len(word)-1)
    status_list[lrandom_index] = word[lrandom_index]
    status_list = ''.join(status_list)

    return status_list


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    
    for i in range(len(original_word)):
        if answer_word[i] == "_" and original_word[i] == char:
            return True
    return False 

# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    
    answer_word = list(answer_word)
    temp_list = list(original_word)

    for letter in original_word:
        index = original_word.index(letter)
        if answer_word[index] == '_':
            temp_list[index] = letter
        else:
            temp_list[index] = '_'
    
    if char in temp_list:
        index = temp_list.index(char)
        answer_word[index] = char

    answer_word = ''.join(answer_word)
    return answer_word


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    
    #if number_guesses >= 0 and not answer:
    print('Wrong! Number of guesses left:',str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):

    print("/----")
    print("|" + ("   0" if number_guesses <= 3 else ""))
    print("|" + ("  /|\\" if number_guesses <= 2 else ""))
    print("|" + ("   |" if number_guesses <= 1 else ""))
    print("|" + ("  / \\" if number_guesses < 1 else ""))
    print("_______")


# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):

    print("Guess the word: " + str(answer))
    number_guesses = 4
    while number_guesses >= 0:
        guess = get_user_input()
        if guess == "quit" or guess == "exit":
            print("Bye!")
            break
        elif is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
            if answer == word:
                break
        else:
            do_wrong_answer(answer, number_guesses)
            number_guesses -= 1
            
        if number_guesses < 0:
            print("Sorry, you are out of guesses. The word was: " + word)


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

