def convert(text):
    text = text.replace(":(", "🙁")
    text = text.replace(":)", "🙂" )
    return text


def main():
    text = input("Type: ")
    converted_text = convert(text)
    print(converted_text)

if __name__ == "__main__":
    main()