'''
Created on 19.04.2022

@author: philipp schroeter
'''

import random
import requests

class wordleWord():

    def __init__(self):
        self.wordle_list_eng = "https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/28804271b5a226628d36ee831b0e36adef9cf449/wordle-answers-alphabetical.txt"

    def get_new_word(self):
        wordle_words = requests.get(self.wordle_list_eng)
        #print(wordle_words.content)
        words_list = wordle_words.content.decode("utf-8").split("\n")
        #print(words_list)
        searched_word = words_list[random.randint(0, len(words_list))]
        #print("searched word is " + str(searched_word))
        return searched_word