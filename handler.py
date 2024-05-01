'''
Created on 19.04.2022

@author: philipp schroeter
'''

import os

class inputHandler():

    def __init__(self, tries=5, word="", show_exluded=False, show_hits=False):
        self.tries = tries
        self.not_guessed = True
        self._searched_word = str(word).lower()
        self.word_length = len(self._searched_word)
        self.all_results = []
        self.show_exluded = show_exluded
        self.excluded = set()
        self.show_hits = show_hits
        self.guessed_parts = ["" for x in range(0, self.word_length)]

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
                    self.guessed_parts[i] = guess[i]
                else:
                    result.append("")
            #print("After hits:")
            #print("tmp_word: " + str(tmp_word))
            #print("hits: " + str(hits))
            #then for the lefts characters, check if they appear on the rest
            rest = [x for x in list(range(0, self.word_length)) if x not in hits]
            #print("rest: " + str(rest))
            tmp_searched_word = list(tmp_word)
            #print("tmp_searched_word: " + str(tmp_searched_word))
            for i in rest:
                try:
                    found_letter = tmp_searched_word.index(guess[i])
                    #print("Found letter " + str(guess[i]) + " in tmp_searched_word at position " + str(found_letter))
                    result[i] = "*"
                    self.guessed_parts[i] = "*"
                    hits.append(i)
                    tmp_word[found_letter] = "*"
                    #remove the letter to prevent duplicate finds
                    tmp_searched_word[found_letter] = ""
                except ValueError:
                    if guess[i] not in self.guessed_parts: self.excluded.add(guess[i])
            #print("After occurs:")
            #print("tmp_word: " + str(tmp_word))
            #print("hits: " + str(hits))
            rest = [x for x in list(range(0, self.word_length)) if x not in hits]
            #print("rest: " + str(rest))
            for i in rest:
                result[i] = "-"
                self.guessed_parts[i] = "-"
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
                    print("Congratulations! You got the word: " + (str(self._searched_word) + ". " + str("On your final guess!") if (self.tries - 1) == 0 else "You had " + str(self.tries - 1) + " guess(es) left."))
                    for r in self.all_results:
                        print(r)
                else:
                    self.tries -= 1
                    if self.show_hits:
                        print(str(self.guessed_parts))
                    else:
                        print(str(guess_result))
                    if self.show_exluded: print("Not occurring letters so far: " + str(self.excluded))
                    print(str(self.tries) + " guesses left.")
            else:
                if not guess.isalpha():
                    print("Only letters may be entered. Try again.")
                elif self.word_length != len(guess):
                    print("Your guess is not " + str(self.word_length) + " characters long. Try again.")
        if self.tries <= 0:
            print("Oh, no. You lost. The searched word was " + str(self._searched_word) + ".")
            for r in self.all_results:
                print(r)