def main():
    due = 50
    payed = 0
    change = 0
    accepted_values = [25, 10, 5]
    while True:
        print(f"Amount Due: {due}") #prints amount due
        coin = int(input("Insert Coin: "))
        if coin in accepted_values:
            due = due - coin #checks how much left due
            payed = payed + coin
        if due <= 0: #if due is less than 0, print the change
            change = payed - 50
            print(f"Change Owed: {change}")
            break
        if due > 0:
            continue
        if due == 0:
            break

if __name__ == "__main__":
    main()