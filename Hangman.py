import random


win = False
correct_guess = 0
max_mistakes = 8
mistakes = 0
revealed_letters = []
guessed_letters = []
index = 0
games_played = 0

# A list of words
wordlist = ["zodiac", "stretch", "oxygen", "matrix", "lucky", "kazoo", "gossip", "awkward", "blizzard", "galaxy", "jaywalk", "unknown", "boxcar", "jackpot", "quizzes", "zigzag", "witchcraft", "zombie", "walkway", "pixel", "subway"]


# Chooses a random word from the word list.
word = random.choice(wordlist)


# Definition that splits the hidden word into a list of letters.
def split(word):
    return [char for char in word]


letters = split(word)


# Counts amount of letters
letter_count = len(letters)


# A variable for the list of letters and removes the duplicates.
hidden_letters = list(dict.fromkeys(split(word)))


# Counts amount of letters in word
max_correct = len(hidden_letters)


# Prepares the visual of the hidden word
display_letters = ['_'] * letter_count


# Introduction
print('\nWelcome to Hangman!')

while True:
    if games_played >= 1:
        choice = str(input('\nWould you like to play again? (y/n): ')).lower()

    else:
        choice = str(input('Would you like to play? (y/n): ')).lower()

    if choice == 'y':
        print('\nGood Luck!')

        while not win:
            print('\n' + ''.join(display_letters))
            guess = input(str('Guess a letter: '))

            # If letter is already guessed
            if guess in guessed_letters:
                print(f'You have already guessed "{guess}", go again!')

            else:

                # If letter correct
                if guess in hidden_letters:
                    correct_guess += 1
                    revealed_letters.append(guess)
                    guessed_letters.append(guess)

                    # Updates the displayed letters
                    while guess in letters:
                        index = letters.index(guess)
                        del letters[index]
                        letters.insert(index, '_')
                        del display_letters[index]
                        display_letters.insert(index, guess)

                    # Finished the word
                    if max_correct <= correct_guess:
                        print('\nYou guessed the word!')
                        print('"' + ''.join(display_letters) + '"')
                        games_played += 1
                        win = True

                    else:
                        print(f'"{guess}" was right!')

                # If letter not correct
                else:
                    mistakes += 1
                    guessed_letters.append(guess)

                    # Reached the maximum amount of wrong guesses
                    if mistakes >= max_mistakes:
                        print(f'"{guess}" was wrong and you lost.')
                        print(f'The word was "{word}"')
                        games_played += 1
                        break

                    else:
                        print(f'"{guess}" was wrong.')

    elif choice == 'n':
        print('\nSee you around!')
        break

    else:
        print('\nType "y" for yes, or "n" for no.')