import re

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    '''
    Converts the text into a list of words.
    '''
    word_list = list(filter(lambda word: word != '', split(',.;? ', text.lower())))
    return word_list


def words_longer_than(length, text):
    '''
    Returns a list of words in the text.
    That is longer than the specified length.
    '''
    word_list = list(filter(lambda word: len(word) > length, split(',.;? ', text.lower())))
    return word_list


def words_lengths_map(text):
    '''
    Returns a dictionary that maps out word length.
    To the number of words in the text of that length.
    '''
    word_list = list(filter(lambda word: word != '', split(',.;? ', text.lower())))
    my_dict = {}
    for word in word_list:
        if len(word) in my_dict:
            my_dict[len(word)] += 1
        else:
            my_dict[len(word)] = 1
    return my_dict


def letters_count_map(text):
    '''
    Responsible to take a string of text as input.
    Returns a dictionary that maps each alphabet letter a to z-
    :to the number of times that letter occurs in the text.
    '''
    word_list = list(filter(lambda word: word != '', split(',.;? ', text.lower())))
    my_dict = {
        'a': 0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0,
        'g': 0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0,
        'm': 0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0,
        's': 0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0,
        'y': 0, 'z':0}
    for word in word_list:
        for char in word:
            my_dict[char] += 1
    return my_dict


def most_used_character(text):
    '''
    Reduce that to the letter that occurs the most
    And return that letter.
    '''
    if not text:
        return None
    char_dict = letters_count_map(text)
    most_char = max(char_dict, key=char_dict.get)
    return most_char
