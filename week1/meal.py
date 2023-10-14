def convert(time):
     hours, minutes = time.split(":")
     return float(hours) + float(minutes)/60

def main():
    time = input("What is the time right now? ").strip().lower()
    if 7 <= convert(time) < 8:
        print("breakfast time")
    if 12 <= convert(time) == 13:
        print("lunch time")
    if 18 <= convert(time) < 19:
        print("dinner time")
    else:
        print(" ")

if __name__ == "__main__":
    main()