import random


def getHangmanPic(turn: int):
    HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    return HANGMANPICS[turn]


def checkWord(word):
    return not ('_' in word)


def setup(turn: int, guessWord: list, usedLetters: list):
    print(getHangmanPic(turn))
    print("Letters you've already tried(don't try to guess a letter more than once): " + ", ".join(usedLetters))
    print(*guessWord)


def main():
    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()
    chosenWord = random.choice(words)
    turn = 0
    guessWord = ['_'] * len(chosenWord)
    usedLetters = []

    print(f"Welcome to Hangman Game! Your goal is to guess the word I've chosen consisting of {len(chosenWord)} letters!")

    while turn < 6:
        setup(turn, guessWord, usedLetters)
        guess = input("Guess a letter: ")
        if len(guess) != 1 or guess in usedLetters:
            print("Input is not correct! Try again")
            continue

        if guess in chosenWord:
            guessWord[chosenWord.index(guess)] = guess
            usedLetters.append(guess)
        else:
            turn += 1
            usedLetters.append(guess)

        if checkWord(guessWord):
            print(f'You win! The word was \"{chosenWord}\"')
            return

    print(getHangmanPic(turn))
    print(f'You lost! The word was \"{chosenWord}\"')


if __name__ == '__main__':
    main()
