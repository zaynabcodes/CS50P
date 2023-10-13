#map allows you to apply some function to every element of a sequence
#Examnple: uppercased = map(str.upper, words)
#list comprehensions is the abilty to construct a list in on line

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words] #list comprehension
    print(*uppercased)

if __name__ == "__main__":
    main()