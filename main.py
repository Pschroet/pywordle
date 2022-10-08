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
    parser.add_argument("-f", "--file", action="store", help="A file with a word list (has higher priority if passed than URL)")
    parser.add_argument("-u", "--url", action="store", help="A url to a file with a word list (has lower priority than file)", default="https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/28804271b5a226628d36ee831b0e36adef9cf449/wordle-answers-alphabetical.txt")
    args = parser.parse_args()
    wordle_word = None
    if hasattr(args, "file"):
        wordle_word = word.get_new_word_from_file(args.file)
    elif hasattr(args, "url"):
        wordle_word = word.get_new_word_from_url(args.url)
    if wordle_word is not None:
        if hasattr(args, "loop") and args.loop:
            print("Running in a loop. Exit with Ctrl+Q.")
            do_run = True
            while do_run:
                try:
                    input_handler = handler.inputHandler(word=wordle_word, show_exluded=args.excluded, show_hits=args.show_hits)
                    input_handler.start()
                except KeyboardInterrupt:
                    do_run = False
                    print(os.linesep + "Exiting guessing... (Just fyi the word was " + str(wordle_word) + ")")
        else:
            input_handler = handler.inputHandler(word=wordle_word, show_exluded=args.excluded, show_hits=args.show_hits)
            input_handler.start()
    else:
        print("Can't start game, because no word was returned")