"""
Filename: WGLib.py
Author: Hannah Shin

"""



def promptPlayAgain():
    """
    Prompts the user to enter either `y` or `n`.
    If the user enters an invalid string,
        a response including the word "invalid" is printed and
        then the user is reprompted for a valid string.
    Must print a message before each user input (either with `print()` or `input()`)
        and prints a message that informs the user of invalid input when they
        provide something other than `y` or `n`.
    
    :returns: `True` if `y` is entered, `False` if `n` is entered.
    """

    # Your code here
    answer = input("Would you like to play again? (y/n): ")
    while answer != 'y' and answer != 'n':
        print("Invalid input, please enter y or n.")
        answer = input("Would you like to play again? (y/n): ")
    return answer == 'y'

def validate(x, start_letter, word_list, used_words):
    """
    Returns `True` if the given word x starts with start_letter, exists in word_list, and is not in used_words (it has not been
    already used in the game).

    :param x: The word to validate.
    :param start_letter: The letter that the word x must start with.
    :param word_list: The list of valid English words.
    :param used_words: The set of words that have already been used.
    :returns: `True` if and only if the given input `x` is deemed "valid".

    An arbitrary (failing) doctest for you to replace is included below:
    >>> validate('ear', 'e', ['ear', 'blue', 'whale'], ['blue'])
    True
    >>> validate('digital', 'e', ['ear', 'digital', 'duke'], ['ear'])
    False
    """
    # Your code here
    return x[0] == start_letter and x in word_list and x not in used_words

def getValidInput(start_letter, word_list, used_words):
    """
    Prompts the user to enter a string word that starts with `start_letter`.
    If the user enters an invalid string - a word that does not start with 'start_letter', is not a real word, or is a repeat of another word,
    then the response displayed will be:
        "invalid word! It must start with the correct letter, be a real word, and not already be used."
    If the word is valid, the function will return the word.

    :param start_letter: The letter that the word x must start with.
    :param word_list: The list of valid English words.
    :param used_words: The set of words that have already been used.
    
    :returns: A string `x` for which `validate(x)` is `True`, where `validate()` is your function in this module.
    """

    # Your code here
    word = input(f"Enter a word starting with '{start_letter}': ")
    while not validate(word, start_letter, word_list, used_words):
        print("invalid word! It must start with the correct letter, be a real word, and not already be used.")
        word = input(f"Enter a word starting with '{start_letter}': ")
    return word

def selectWords(words, num, start_letter):
    """
    Given a list of strings `words`, a non-negative integer `num`, and a lowercase letter `start_letter`, display only
    the words that start with `start_letter`.
        If 'num' is  0 or 'num' is greater than the number of words that start with 'start_letter', all filtered words are returned.
        Otherwise, only 'num' are returned.


    :param words: A list of strings, assumed to be lowercase English words (as in `lowerwords.txt`).
    :param num: The number of strings desired, except when `num==0`, in which case there is no bound.
                As many valid strings, up to `num`, will be returned.
    :param start_letter: The first letter of the next word needs to start with the last letter of the word before it.
    :returns: A list of selected strings as defined above.

    Some example doctests for you to replace are included below:
    >>> selectWords(['duke', 'blue', 'devil', 'spice', 'eared', 'print'], 0, 'd')
    ['duke', 'devil']
    >>> selectWords(['spice', 'eared'], 1, 's')
    ['spice']
    """

    # Your code here
    satisfying = [w for w in words if w[0] == start_letter]
    if num == 0 or num >= len(satisfying):
        return satisfying
    return satisfying[:num]

def createDisplayString(used_words, score, start_letter):
    '''

    Constructs and returns a string displaying the current game state, including
    the words used so far, the player's current score, and the letter the next
    word must start with.

    :param used_words: The set of words that have already been used.
    :param score: The current score of the game state.
    :param start_letter: The first letter of the next word needs to start with the last letter of the word before it.
    :returns: A string that describes the provided state of the game (as parameters).
    >>> createDisplayString(['happy','yellow'], 11, 'w')
    'Words so far: happy -> yellow\nScore: 11\nNext word must start with: w'
    >>> createDisplayString(['chills', 'splendid'], 14, 'd')
    'Words so far: chills -> splendid\nScore: 14\nNext word must start with: d'
    '''
    #Your code here
    return "Words so far: " + ' -> '.join(used_words) + "\nScore: " + str(score) + "\nNext word must start with: " + start_letter



def processValidInput(word, used_words, score):
    '''
    Updates the game state after a valid word is entered. Adds the word to used_words and increments
    the score by the length of the word, and returns the last letter of the word to be used as the
    starting letter on the next turn.

    :param word: A valid word entered by the user.
    :param used_words: A list of words already used in the current game, which will be mutated.
    :param score: The current score of the game. The score is calculated by adding the length of the valid word to the current score.
    :returns: A tuple of (new_score, last_letter) after processing the word.

    >>> used = ['blue', 'devil']
    >>> processValidInput('ear', used, 0)
    (3, 'r')
    >>> used
    ['blue', 'devil', 'ear']
    >>> used2 = ['ear', 'devil']
    >>> processValidInput('blue', used2, 3)
    (7, 'e')
    >>> used2
    ['ear', 'devil', 'blue']
    '''
    used_words.append(word)
    score += len(word)
    return (score, word[-1])

def parseWordsFile(wordsFilePath):
    """
    Given the path to a file with one word per line, return a list of those words in the order in which they were read,
        omitting any trailing whitespace or newline characters. Do NOT call `selectWords()` in this function!

    :param wordsFilePath: A string that is the path to a plaintext file containing one English word per line.
    :returns: A list of the strings in the file at `wordsFilePath`.

    >>> words = parseWordsFile('lowerwords.txt'); words[9323]
    'computer'
    >>> words = parseWordsFile('lowerwords.txt'); words[36096]
    'science'
    """

    #Your code here
    words = []
    file = open(wordsFilePath)
    for line in file:
        words.append(line.strip())
    file.close()
    return words

if __name__ == "__main__":
    import doctest
    doctest.testmod() # runs the doctests in your docstrings above