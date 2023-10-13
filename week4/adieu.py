names = []#stores names

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

if len(names) == 1:
  only_name = names[0]
  print(f"Adieu, adieu, to {only_name}")
elif len(names) == 2:
   names_str = names[0]
   last_name = names[-1]
   print(f"Adieu, adieu, to {names_str} and {last_name}.")
else:
  names_str = ", ".join(names[:-1])
  last_name = names[-1]
  print(f"Adieu, adieu, to {names_str}, and {last_name}.")