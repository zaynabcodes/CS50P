import math

def main(fraction):
    try:
        percentage = convert(fraction)
        fuel = gauge(percentage)
        return fuel
    except ValueError:
        return "Invalid input"
    except ZeroDivisionError:
        return "Cannot divide by zero"

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x > y:
            raise ValueError

        if y == 0:
            raise ZeroDivisionError

    except ValueError:
        raise ValueError

    percentage = (x // y) * 100
    return percentage

def gauge(percentage):
    percentage = int(percentage)

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
