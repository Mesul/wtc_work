#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    f = open(file_name, 'r')
    fr = f.readlines()
    f.close()

    return (fr)


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    rn = random.randint(0, len(words) - 1)
    r_word = words[rn]

    rn2 = random.randint(0, len(r_word) - 1)
    w_list = list(r_word)
    w_list[rn2] = '_'
    w_list = ''.join(w_list)

    print("Guess the word: " + w_list)

    return r_word


def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    empty_spaces = input("Guess the missing letter: ")

    return empty_spaces



def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

