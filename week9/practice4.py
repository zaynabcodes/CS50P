#type hints are a way to specify what type of variable you want the value to be
#mypy is a program that checks withever or not your code is adhereing to your type hints, with pip install mypy

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")