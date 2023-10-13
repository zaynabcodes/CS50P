#generators

def main():
    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    return "sheep" * n

if __name__ == "__main__":
    main()