'''
Created on 19.04.2022

@author: philipp schroeter
'''

import handler
import word

if __name__ == '__main__':
    wordle_word = word.wordleWord()
    input_handler = handler.inputHandler(word=wordle_word.get_new_word())
    input_handler.start()