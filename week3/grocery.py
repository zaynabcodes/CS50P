item_dict = {}#creates a dictionary

while True:#continues loop as long as true
    try:
        item = input()#stores input into variable, item
        if item:
            item_lower = item.lower()#changes item to lowercase
            if item_lower in item_dict:
                item_dict[item_lower] += 1#if the item is in the dictionary, adds an increment of 1
            else:
                item_dict[item_lower] = 1#if already is there adds another 1
    except EOFError:#if user types control d, exit out of loop
        break

sorted_items = sorted(item_dict.items())#sorts dictionary item
for item, count in sorted_items:
    print(f"{count} {item.upper()}")#prints the items count followed by item name
