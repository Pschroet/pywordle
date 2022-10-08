'''
Created on 19.04.2022

@author: philipp schroeter
'''

import os
import random
import requests

def get_new_word_from_file(file=None, debug=False):
    if file is not None and os.path.isfile(file):
        wordle_words = open(file).read()
        words_list = wordle_words.split(os.linesep)
        #print(words_list)
        searched_word = words_list[random.randint(0, len(words_list))]
        if debug: print("searched word is " + str(searched_word))
        return searched_word
    return None

def get_new_word_from_url(url=None, debug=False):
    wordle_words = requests.get(url)
    #print(wordle_words.content)
    words_list = wordle_words.content.decode("utf-8").split("\n")
    #print(words_list)
    searched_word = words_list[random.randint(0, len(words_list))]
    if debug: print("searched word is " + str(searched_word))
    return searched_word