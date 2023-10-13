def main():
    greeting = input("What is your greeting?: ").lower().strip()
    amount = value(greeting)
    print(amount)



def value(greeting):
    if greeting.startswith("hello"):
        greeting = 0
    elif greeting.startswith("h"):
        greeting = 20
    else:
        greeting =  100
    return greeting


if __name__ == "__main__":
    main()