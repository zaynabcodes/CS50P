#Docstrings is a standarized way how you should document your functions, inside of the function with three "

def meow(n: int) -> str:
    """
    Meow n times

    :param n: Number of times to meow
    :type n: int
    :raise TypeError
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")