'''
Created on 19.04.2022

@author: philipp schroeter
'''

import argparse
import handler
import word

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--excluded", action="store_true", default=False, help="show a list with the wrong letters after each guess")
    parser.add_argument("-s", "--show_hits", action="store_true", default=False, help="show the hits in an extra list after each guess")
    args = parser.parse_args()
    wordle_word = word.wordleWord().get_new_word()
    input_handler = handler.inputHandler(word=wordle_word, show_exluded=args.excluded, show_hits=args.show_hits)
    input_handler.start()