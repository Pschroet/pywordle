'''
Created on 19.04.2022

@author: philipp schroeter
'''

import argparse
import handler
import os
import word

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--excluded", action="store_true", default=False, help="show a list with the wrong letters after each guess")
    parser.add_argument("-s", "--show_hits", action="store_true", default=False, help="show the hits in an extra list after each guess")
    parser.add_argument("-l", "--loop", action="store_true", default=False, help="Run in a loop, quit with Ctrl+Q")
    args = parser.parse_args()
    if hasattr(args, "loop") and args.loop:
        print("Running in a loop. Exit with Ctrl+Q.")
        do_run = True
        while do_run:
            try:
                wordle_word = word.wordleWord().get_new_word()
                input_handler = handler.inputHandler(word=wordle_word, show_exluded=args.excluded, show_hits=args.show_hits)
                input_handler.start()
            except KeyboardInterrupt:
                do_run = False
                print(os.linesep + "Exiting guessing... (Just fyi the word was " + str(wordle_word) + ")")
    else:
        wordle_word = word.wordleWord().get_new_word()
        input_handler = handler.inputHandler(word=wordle_word, show_exluded=args.excluded, show_hits=args.show_hits)
        input_handler.start()