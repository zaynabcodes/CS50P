import re

def main():
    print(count(input("Text: ")))


def count(s):
    word1 = "um"
    word2 = "Um"
    pattern = fr"({word1}|{word2})"
    check = re.findall(r"\b" + pattern + r"\b", s)
    return len(check)

if __name__ == "__main__":
    main()