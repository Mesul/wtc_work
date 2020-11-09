import unittest
from unittest.mock import patch
from io import StringIO
import word_processor


class MyTestCase(unittest.TestCase):
    def test_convert_to_word_list(self):
        self.assertEqual(word_processor.convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?'), ['these', 'are', 'indeed', 'interesting', 'an', 'obvious', 'understatement', 'times', 'what', 'say', 'you'])
        self.assertEqual(word_processor.convert_to_word_list('I am a programmer in the pipeline'), ['i', 'am', 'a', 'programmer', 'in', 'the', 'pipeline'])
        self.assertEqual(word_processor.convert_to_word_list('To be or not to be that is the question'), ['to', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'])


    def test_words_longer_than(self):
        self.assertEqual(word_processor.words_longer_than(10, 'These are indeed interesting, an obvious understatement, times. What say you?'), ['interesting', 'understatement'])
        self.assertEqual(word_processor.words_longer_than(5, 'I am a programmer in the pipeline'), ['programmer', 'pipeline'])
        self.assertEqual(word_processor.words_longer_than(3, 'To be or not to be that is the question'), ['that', 'question'])
    
    
    def test_words_lengths_map(self):
        self.assertEqual(word_processor.words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?'), {5: 2, 3: 3, 6: 1, 11: 1, 2: 1, 7: 1, 14: 1, 4: 1})
        self.assertEqual(word_processor.words_lengths_map('To be or not to be that is the question'), {2: 6, 3: 2, 4: 1, 8: 1})
        self.assertEqual(word_processor.words_lengths_map('I am a programmer in the pipeline'), {1: 2, 2: 2, 10: 1, 3: 1, 8: 1})

    def test_letters_count_map(self):
        self.assertEqual(word_processor.letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?'), {'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0})
        self.assertEqual(word_processor.letters_count_map('To be or not to be that is the question'), {'a': 1, 'b': 2, 'c': 0, 'd': 0, 'e': 4, 'f': 0, 'g': 0, 'h': 2, 'i': 2, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 2, 'o': 5, 'p': 0, 'q': 1, 'r': 1, 's': 2, 't': 7, 'u': 1, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0})
        self.assertEqual(word_processor.letters_count_map('I am a programmer in the pipeline'), {'a': 3, 'b': 0, 'c': 0, 'd': 0, 'e': 4, 'f': 0, 'g': 1, 'h': 1, 'i': 4, 'j': 0, 'k': 0, 'l': 1, 'm': 3, 'n': 2, 'o': 1, 'p': 3, 'q': 0, 'r': 3, 's': 0, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0})


    def test_most_used_character(self):
        self.assertEqual(word_processor.most_used_character('These are indeed interesting, an obvious understatement, times. What say you?'), "e")
        self.assertEqual(word_processor.most_used_character('To be or not to be that is the question'), "t")
        self.assertEqual(word_processor.most_used_character('I am a programmer in the pipeline'), "e")
        self.assertEqual(word_processor.most_used_character(''), None)


if __name__ == "__main__":
    unittest.main()
    