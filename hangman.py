# Problem Set 2, hangman.py
# Name: Karen Andre
# Collaborators: None
# Time spent: 3:00

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.    
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letter_in_list = True # checks if current letter is in guessed list
    for i in secret_word:
      if not(i in letters_guessed):
        letter_in_list = False
    return letter_in_list


def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and plus signs (+) that represents
        which letters in secret_word have not been guessed so far
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_array = []
    for letter in secret_word:
      if letter in letters_guessed:
        word_array.append(letter)
      else:
        word_array.append("+")
    word_guessed = ''.join(word_array)
    return word_guessed
    


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = list(string.ascii_lowercase)
    for letter in letters_guessed:
      if letter in available_letters: # need to check this to avoid errors
        available_letters.remove(letter)
    return ''.join(available_letters)



def letter_reveal(secret_word, available_letters):
    '''
    secret_word: string, the secret word to guess.
    available_letters: string, letters that have not been guessed yet

    returns: char, random letter to be revealed
    '''
    choose_from = []
    for letter in secret_word:
      if letter in available_letters:
        choose_from.append(letter)
    choose_from = ''.join(choose_from)
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter

    

def hangman(secret_word, with_help):
    '''
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # variables
    guesses_left = 10
    available_letters = string.ascii_lowercase
    letters_guessed = []
    word_progress = get_word_progress(secret_word, letters_guessed)
    vowels = 'aeiou'

    # welcome the user
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    # game runs while there are guesses left and the player has not won
    while guesses_left > 0 and not(has_player_won(secret_word, letters_guessed)):
      print("--------") # used to separate guesses
      print(f"You have {guesses_left} guesses left.")
      print(f"Available letters: {available_letters}")
      current_guess = input("Please guess a letter: ")
      # makes the guess lowercase
      if current_guess.isalpha():
        current_guess = current_guess.lower()
      # user requests help and help is allowed
      if current_guess == '!' and with_help:
        if guesses_left < 3:
          print(f"Oops! Not enough guesses left: {word_progress}")
        else:
          current_guess = letter_reveal(secret_word, available_letters)
          letters_guessed.append(current_guess)
          available_letters = get_available_letters(letters_guessed)
          word_progress = get_word_progress(secret_word, letters_guessed)
          print(f"Letter revealed: {current_guess}")
          print(word_progress)
          guesses_left -= 3
      # invalid guess
      elif len(current_guess) != 1 or not current_guess.isalpha():
        print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {word_progress}")
      # already guessed
      elif current_guess in letters_guessed:
        print(f"Oops! You've already guessed that letter: {word_progress}")
      # wrong guess
      elif current_guess not in secret_word:
        if current_guess in vowels:
          guesses_left -= 2
        else:
          guesses_left -= 1
        letters_guessed.append(current_guess)
        available_letters = get_available_letters(letters_guessed)
        print(f"Oops! That letter is not in my word: {word_progress}")
      # correct guess
      elif current_guess in secret_word:
        letters_guessed.append(current_guess)
        available_letters = get_available_letters(letters_guessed)
        word_progress = get_word_progress(secret_word, letters_guessed)
        print(f"Good guess: {word_progress}")

    print("--------")
    if (has_player_won(secret_word, letters_guessed)):
      unique_array = []
      unique_count = 0
      for letter in secret_word:
        if letter not in unique_array:
          unique_array.append(letter)
          unique_count += 1
      total_score = (4 * unique_count * guesses_left) + (2 * len(secret_word))
      print("Congratulations, you won!")
      print(f"Your total score for this games is: {total_score}")
    else:
      print(f"Sorry, you ran out of guesses. The word was {secret_word}")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following two lines.
       secret_word = choose_word(wordlist)
       with_help = True
       hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.