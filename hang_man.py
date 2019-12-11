from colorama import init
from termcolor import colored
from linereader import copen
from random import randint
import time
# E:\Itay\Python\hang_man.py
# F:\Itay\Python\hang_man.py
global letter_garbage
global the_abc
global HANGMAN
letter_garbage = {}
the_abc = "abcdefghijklmnopqrstuvxwyz" #?
for letter in the_abc:
	letter_garbage[letter] = "Unknown"
HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")
# Maybe I will add best results table

def random_word():
	# credit to https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/
	words_list = copen(r"C:\Users\itays\OneDrive\Desktop\Usb-backup\Itay\Python\the_most_commons_words_in_english.txt")
	# credit to https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python
	lines = words_list.count('\n')
	word = words_list.getline(randint(1, lines))
	word = word.split("\n")[0]
	words_list.close()
	return word

def guess_legal_letter():
	try:
		letter = input("Guess a letter that you didn't guess before: ").lower()
		while not letter_garbage[letter] == "Unknown":
				letter = input("Guess a letter that you didn't guess before: ").lower()
		return letter
	except Exception:
		return guess_legal_letter()
		
def my_round(word_in_list, guess_in_list):
	print_guess(guess_in_list) 
	try:
		letter = input("Guess a letter: ").lower()
		if not letter_garbage[letter] == "Unknown":
			letter = guess_legal_letter()
	except Exception:
		letter = guess_legal_letter()
	if letter in word_in_list:
		guess_in_list = show_letter(guess_in_list, letter, word_in_list)
		letter_garbage[letter] = True
		if word_guessed(guess_in_list): # guess_in_list == word_in_list
			return "Win"
	else:
		letter_garbage[letter] = False
	wrong_letters = false_in_list(letter_garbage)
	lost = draw_hangman(wrong_letters)
	print_letter_garbage()
	if lost:
		return "Lose"
	else:
		return "Game in progress"
	
def print_guess(guess):
	for letter in guess:
		if letter == "":
			print("*", end = "")
		else:
			print(letter, end = "")
	print("")

def game(word):
	result = "Game in progress"
	word_in_list = word_to_list(word)
	guess_in_list = []
	for cell in word_in_list:
		guess_in_list.append("")
	while result == "Game in progress":
		result = my_round(word_in_list, guess_in_list)
	if result == "Win":
		print("Great, you won!")
	else:
		print("Oh no, you lost! \nmaybe you will win in the next time!")
	print('The word was "' + word + '".')

def show_letter(guess_in_list, letter, word_in_list):
	for i in range(0, len(word_in_list)):
		if word_in_list[i] == letter:
			guess_in_list[i] = letter
	return guess_in_list

def word_to_list(word):
	word_in_list = []
	for letter in word:
		word_in_list.append(letter)
	return word_in_list
		
def false_in_list(list):
	count = 0
	for cell in list:
		if not list[cell]:
			count += 1
	return count

def draw_hangman(wrong_letters):
	#credit to https://codereview.stackexchange.com/questions/95997/simple-game-of-hangman
	if wrong_letters < 10:
		print(HANGMAN[wrong_letters])
		return False
	else:
		print(HANGMAN[10])
		return True
		
	
def print_letter_garbage():
	for letter in the_abc:
		if letter_garbage[letter] == "Unknown":
			print(letter, end = " ")
		elif letter_garbage[letter]:
			print(colored(letter, "green"), end = " ")
		else:
			print(colored(letter, "red"), end = " ")
	print("")

def word_guessed(word_in_list):
	for cell in word_in_list:
		if cell == "":
			return False
	return True

if __name__ == '__main__':
	start_time = time.time()
	word = random_word()
	init()
	game(word)
	time_from_start = round(time.time() - start_time, 2)
	print("The game took %s seconds" % time_from_start)
	