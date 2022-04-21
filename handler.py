'''
Created on 19.04.2022

@author: philipp schroeter
'''

import os

class inputHandler():

    def __init__(self, tries=5, word=""):
        self.tries = tries
        self.not_guessed = True
        self.searched_word = str(word).lower()
        self.word_length = len(self.searched_word)

    def start(self):
        all_results = []
        #print("Searched word: " + str(self.searched_word))
        print("The searched word has a length of " + str(self.word_length) + ".")
        while self.tries > 0 and self.not_guessed:
            guess = str(input("Your guess: ")).lower()
            #check if only legal characters are entered
            if guess.isalpha():
                if self.word_length == len(guess):
                    result = []
                    hits = []
                    tmp_word = list(self.searched_word)
                    #first check direct hits, record the hit positions and build the results list
                    for i in range(0, self.word_length):
                        if guess[i] == self.searched_word[i]:
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
                        found_letter = self.searched_word.find(guess[i])
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
                    all_results.append(result)
                    if "-" not in result and "*" not in result:
                        self.not_guessed = False
                        print("Congratulations! You got the word: " + str(self.searched_word) + ". You had " + str(self.tries) + " guesses left.")
                        for r in all_results:
                            print(r)
                    else:
                        self.tries -= 1
                        print(str(result) + os.linesep + str(self.tries) + " guesses left.")
                else:
                    print("Your guess is not " + str(self.word_length) + " characters long. Try again.")
            else:
                print("Only letter may be entered. Try again.")
        if self.tries < 0:
            print("Oh, no. You lost. The searched word was " + str(self.searched_word) + ".")
            for r in all_results:
                print(r)