import re
import time
from random_word import RandomWords

r = RandomWords()

#variable with all hangman boards
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Start timer
def start_timer():
    return time.time()

# End timer
def end_time(start_time):
    return time.time() - start_time

# Randomizes a word
def get_random_word():
    word = r.get_random_word()
    return word

# Check if the letter is a letter
def check_letter(letter):
    if re.match(r"^[a-zA-Z]$", letter):
        return True
    else:
        print("You must enter a letter")
        return False

# Displays the board and handles the game logic
def play_hangman(word):
    start_time = start_timer() #starts the timer
    blanks = "_" * len(word) #calculates the amou ntof blanks
    wrong_guesses = 0

    while True:
        print(HANGMANPICS[wrong_guesses]) #while true the hangman pic with print out depending on the amoung of wrong guesses
        print(blanks) # prints the blanks
        letter = input("Letter: ").lower()

        if not check_letter(letter): #checks if the letter is not a letter
            continue

        if letter in word: #checks if letter is in word
            new_blanks = "" #supposed to store the updated version of blanks
            for i in range(len(word)): #runs as long as the length of the word
                if word[i] == letter: #checks if the character at index i in the word matches the letter
                    new_blanks += letter #if so the letter is added to the new blanks
                else:
                    new_blanks += blanks[i] #if not it adds the character from the blanks at index i to the new blanks, to store the previous correct guesses
            blanks = new_blanks
        else:
            wrong_guesses += 1 #if the letter is wrong increments by 1

        #displays the congratulation message
        if blanks == word:
            end = end_time(start_time)
            end = round(end, 2)
            print(f"Congrats, you guessed the word '{word}' in {end} seconds!")
            break

        #displays the failure message
        if wrong_guesses == 6:
            end = end_time(start_time)
            end = round(end, 2)
            print(f"Game ended in {end} seconds. The word was '{word}'")
            break

def main():
    random_word = get_random_word()
    play_hangman(random_word)

if __name__ == "__main__":
    main()
