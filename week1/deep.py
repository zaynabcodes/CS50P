response = str(input("What is the Great Question of Life, the Universe and Everything: ")).lower().strip()

match response:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")