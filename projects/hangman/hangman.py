import random
from words import words
import string

# print(words)


def getValidWords(words):
    word = random.choice(words)  # randomly choose any word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = getValidWords(words)
    wordLetters = set(word)  # set#letters in the word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()  # set#what letter the user has guessed

    lives = 6

    print("****************************************************************************************")
    print("*                                                                                      *")
    print("*                                                                                      *")
    print("*                                                                                      *")
    print("*                               Welcome To Hangman Game!                               *")
    print("*                                                                                      *")
    print("*                                                                                      *")
    print("*                                                                                      *")
    print("****************************************************************************************")
    print("\n\n\n")

    # Getting User Input
    while len(wordLetters) > 0 and lives > 0:
        # letter used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have ", lives,
              "lives left and You have used these letters: ", ' '.join(usedLetters))

        # what current word is(ie: W - R D)
        wordList = [
            letter if letter in usedLetters else '-' for letter in word]
        print("\nCurrent word: ", " ".join(wordList))

        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives -= 1
                print("Letter is not in the word")

        elif userLetter in usedLetters:
            print("You have alredy used this character. Please try again.")

        else:
            print("Invalid Character. Please try again.")

    # gets here when len (wordLetters) == 0 OR when livves == 0

    if lives == 0:
        print("\nSorry, you have died. The word was", word, "\n")
    else:
        print("\nYou have guessed the word correctly. The word is ", word, "!!!\n")


hangman()  # call the main function
