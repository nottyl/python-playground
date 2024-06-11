"""
An implementation of Bagels by Al Sweigart
"""

import random

MAX_DIGITS = 3
MAX_GUESSES = 10


def main():
    print("Bagels - A deductive logic game.")
    print("I am thinking of a {}-digit with no repeated digits".format(MAX_DIGITS))  # noqa: E501
    print("When I say:        That Means:")
    print("Pico      :        One digit is in the wrong position.")
    print("Fermi     :        One digit is in the right position.")
    print("Bagels    :        No digit is correct.")

    while True:
        secretNum = getSecretNum()
        print("I have thought of the number :)")
        print("You have {} guesses to get it".format(MAX_GUESSES))
        guessCount = 1
        while guessCount <= MAX_DIGITS:
            guess = ""
            while len(guess) != MAX_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(guessCount))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            guessCount += 1

            if guess == secretNum:
                break
            if guessCount > MAX_GUESSES:
                print("You ran out of guesses")
                print("The answer was {}.".format(secretNum))

        print("Do you want to play again? (y/n)")
        if not input("> ").lower().startswith('y'):
            break
        print("Thanks for playing!")


def getSecretNum():
    # This is a list of digits 0 to 9
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(MAX_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return "That's correct!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return "".join(clues)


# If the program is run (instead of imported), run the game
if __name__ == '__main__':
    main()
