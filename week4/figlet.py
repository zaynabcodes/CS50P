#imports modules
import sys
import random
from pyfiglet import Figlet

#randomizes font
def get_random_font():
    return random.choice(Figlet.getFonts())

#set the fonts for both statements
def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        font = get_random_font()
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        fonts = figlet.getFonts()
        arg = sys.argv[2]
        if arg in fonts:
            font = arg
    else:
        print("Invalid usage")
        sys.exit(1)

    user_input = input("Input: ")
    figlet.setFont(font=font)
    result = figlet.renderText(user_input)
    print(result)

if __name__ == "__main__":
    main()

