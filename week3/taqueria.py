#Menu
food = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#stores the current order total
total = 0.00
ordered_items = []
while True:
        try:
            item = input("Item: ").title()#Asks user for item and capitalizes the first letter
            if item in food: #checks if item is in food
                ordered_items.append(item)
                total += food[item] #sets total equal to value of item
                print(f"Total:  ${total:.2f}")#prints the new total
        except EOFError:#sets a except for if user does control + d
            print(f"Total:  ${total:.2f}")#prints the new total
            break