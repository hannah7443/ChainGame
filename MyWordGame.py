"""
Filename: MyWordGame.py
Author: Hannah Shin

"""

import WGLib
import random # to set the random seed

def playGame(words):
    """
    This function sets up the game, runs each round/turn, then returns a non-negative
        integer representing the player's score.

    :param words: A list of strings, each string containing exactly one word composed of letters of the Latin alphabet (a-z).
    :returns: The player's score at the end of a game. If the game has only two conclusions, win or lose, consider 0 for lose and 1 for win.
    """
    # asks the player how many turns they want to play
    num_turns = input("How many turns would you like to play? ")
    while not num_turns.isdigit() or int(num_turns) <= 0:
        print("Invalid input, please enter a positive number.")
        num_turns = input("How many turns would you like to play? ")
    num_turns = int(num_turns)

    # Initialize game state
    word_list = WGLib.parseWordsFile('lowerwords.txt')
    used_words = []
    score = 0
    turns_left = num_turns
    start_word = input("Which word would you like to start with?")
    while start_word not in word_list:
        print("Invalid input, please enter a real word.")
        start_word = input("Which word would you like to start with?")
    used_words.append(start_word)
    start_letter = start_word[-1]

    # game loop
    while turns_left > 0:
        print(WGLib.createDisplayString(used_words, score, start_letter))
        word = WGLib.getValidInput(start_letter, word_list, used_words)
        result = WGLib.processValidInput(word, used_words, score)
        score = result[0]
        start_letter = result[1]
        turns_left -= 1

    # end of game
    print("Game over!")
    print("Words played: " + ' -> '.join(used_words))
    print("Final score: " + str(score))
    return score


def startSession(words, seed=None):
    '''
    This function facilitates an interactive session, allowing the user to play your game multiple times.

    :param words: A list of strings, each string containing exactly one word composed of letters of the Latin alphabet (a-z).
    :param seed: (default 101) An integer to be used by random.seed() to set the so-called `seed` of its
        pseudo-random number generator. By setting the seed to a fixed value (e.g., 101), the random values obtained
        will be consistent across multiple runs of the same program. We set this for you; see the top two lines.
        If this value is None (or False), then the seed will change each time this function is called (as is usually intended).
        
    '''

    if seed:
        random.seed(seed) # DO NOT REMOVE OR CALL THIS METHOD ANY OTHER WAY!
    scores = []

    score = playGame(words)
    scores.append(score)

    # Keep asking to play again
    while WGLib.promptPlayAgain():
        score = playGame(words)
        scores.append(score)

    # Print summary
    print("Thanks for playing!")
    print("Number of games played: " + str(len(scores)))
    print("Highest score: " + str(max(scores)))
    print("Average score: " + str(sum(scores) // len(scores)))

    return scores


if __name__ == "__main__":

    # To play a single game:
    random.seed(101) # remove to allow random module to produce different values each run
    words = WGLib.parseWordsFile('lowerwords.txt') # implement this first in WGLib.py (or hard-code your own list of words for testing).
    score = playGame(words)
    print('Your score is: ', score)

    # # To play multiple games in a row, call:
    # words = WGLib.parseWordsFile('lowerwords.txt')
    # scores = startSession(words, 101) # second parameter will be used as the random seed; remove or replace as desired for testing.
    # print('Your scores were:', ", ".join(str(s) for s in scores))