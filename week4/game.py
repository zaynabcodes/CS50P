import random#imports random

while True:
    level = input("Level: ")#asks user for level
    if level.isdigit() and int(level) > 0:#checks if level is an int and if level is greater than 0
        level = int(level)
        break
    else: #if not, ask user for level again
        level = input("Level: ")#asks user for level

secret_num = random.randint(1, level)#randomizes a number from 1 to level

while True:
    guess = input("Guess: ")#asks user for their guess
    if guess.isdigit() and int(guess) > 0:#check if guess is a digit and if guess is greater than 0
        guess = int(guess)#changes guess to an integer

        if guess < secret_num:#check if guess is smaller than number then prints:
            print("Too small!")
        elif guess > secret_num:#checks if guess is greater than number then prints:
            print("Too large!")
        else:#checks if guess is the same as number then prints:
            print("Just right!")
            break
    else:#if all fails, asks for guess again
        guess = input("Guess: ")#asks user for their guess