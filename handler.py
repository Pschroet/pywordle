'''
Created on 19.04.2022

@author: philipp schroeter
'''

import os

class inputHandler():

    def __init__(self, tries=5, word=""):
        self.tries = tries
        self.not_guessed = True
        self._searched_word = str(word).lower()
        self.word_length = len(self._searched_word)
        self.all_results = []

    def _check_guess(self, guess):
        if guess.isalpha() and self.word_length == len(guess):
            result = []
            hits = []
            tmp_word = list(self._searched_word)
            #first check direct hits, record the hit positions and build the results list
            for i in range(0, self.word_length):
                if guess[i] == self._searched_word[i]:
                    result.append("+")
                    hits.append(i)
                    tmp_word[i] = ""
                else:
                    result.append("")
            #then for the lefts characters, check if they appear on the rest
            rest = [x for x in list(range(0, self.word_length)) if x not in hits]
            #print("After hits:")
            #print("tmp_word: " + str(tmp_word))
            #print("rest: " + str(rest))
            for i in rest:
                found_letter = self._searched_word.find(guess[i])
                if found_letter > -1:
                    result[i] = "*"
                    hits.append(i)
                    tmp_word[found_letter] = "*"
            rest = [x for x in list(range(0, self.word_length)) if x not in hits]
            #print("After occurs:")
            #print("tmp_word: " + str(tmp_word))
            #print("rest: " + str(rest))
            for i in rest:
                result[i] = "-"
            self.all_results.append(result)
            return result
        else:
            return None

    def start(self):
        #print("Searched word: " + str(self._searched_word))
        print("The searched word has a length of " + str(self.word_length) + ".")
        while self.tries > 0 and self.not_guessed:
            guess = str(input("Your guess: ")).lower()
            #check if only legal characters are entered
            guess_result = self._check_guess(guess)
            if guess_result is not None:
                if "-" not in guess_result and "*" not in guess_result:
                    self.not_guessed = False
                    print("Congratulations! You got the word: " + str(self._searched_word) + ". You had " + str(self.tries) + " guesses left.")
                    for r in self.all_results:
                        print(r)
                else:
                    self.tries -= 1
                    print(str(guess_result) + os.linesep + str(self.tries) + " guesses left.")
            else:
                if guess.isalpha():
                    print("Only letter may be entered. Try again.")
                elif self.word_length == len(guess):
                    print("Your guess is not " + str(self.word_length) + " characters long. Try again.")
        if self.tries < 0:
            print("Oh, no. You lost. The searched word was " + str(self._searched_word) + ".")
            for r in self.all_results:
                print(r)