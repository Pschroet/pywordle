'''
Created on 21.04.2022

@author: philipp schroeter
'''

from handler import inputHandler
import unittest

class Test(unittest.TestCase):


    def test_correctGuess(self):
        h = inputHandler(tries=1, word="test")
        guess_result = h._check_guess("test")
        self.assertEqual(guess_result, ["+", "+", "+", "+"])

    def test_completelyWrongGuess(self):
        h = inputHandler(tries=1, word="wrong")
        guess_result = h._check_guess("qetzu")
        self.assertEqual(guess_result, ["-", "-", "-", "-", "-"])

    def test_allWrongPositionsGuess(self):
        h = inputHandler(tries=1, word="position")
        guess_result = h._check_guess("ositionp")
        self.assertEqual(guess_result, ["*", "*", "*", "*", "*", "*", "*", "*"])

    def test_halfWrongPositionsGuess(self):
        h = inputHandler(tries=1, word="motors")
        guess_result = h._check_guess("motsor")
        self.assertEqual(guess_result, ["+", "+", "+", "*", "*", "*"])

    def test_duplicateLetterOneCorrectGuess(self):
        h = inputHandler(tries=1, word="motor")
        guess_result = h._check_guess("motro")
        self.assertEqual(guess_result, ["+", "+", "+", "*", "*"])

    def test_duplicateLetterNoneCorrectGuess(self):
        h = inputHandler(tries=1, word="guess")
        guess_result = h._check_guess("ssgue")
        self.assertEqual(guess_result, ["*", "*", "*", "*", "*"])

    def test_shortPalindromeCorrect(self):
        h = inputHandler(tries=1, word="otto")
        guess_result = h._check_guess("otto")
        self.assertEqual(guess_result, ["+", "+", "+", "+"])

    def test_shortPalindromeWrong(self):
        h = inputHandler(tries=1, word="otto")
        guess_result = h._check_guess("toot")
        self.assertEqual(guess_result, ["*", "*", "*", "*"])

    def test_palindromeCorrect(self):
        h = inputHandler(tries=1, word="racecar")
        guess_result = h._check_guess("racecar")
        self.assertEqual(guess_result, ["+", "+", "+", "+", "+", "+", "+"])

    def test_palindromeWrong(self):
        h = inputHandler(tries=1, word="racecar")
        guess_result = h._check_guess("acrerca")
        self.assertEqual(guess_result, ["*", "*", "*", "+", "*", "*", "*"])

    def test_lengthWrong(self):
        h = inputHandler(tries=1, word="one")
        guess_result = h._check_guess("on")
        self.assertEqual(guess_result, None)

    def test_nonAlpha(self):
        h = inputHandler(tries=1, word="one")
        guess_result = h._check_guess("1")
        self.assertEqual(guess_result, None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()