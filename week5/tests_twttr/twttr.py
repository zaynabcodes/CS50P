def main():
    word = input("Input: ")
    word = shorten(word)
    print(f"Output: {word}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]#stores vowels
    letters = []
    for c in word: #checks the character in word
      if c not in vowels: #if the character is not in the vowels
         letters.append(c) #add the character in the letters list
    letters = "".join(letters)
    return letters #and return the letters


if __name__ == "__main__":
    main()