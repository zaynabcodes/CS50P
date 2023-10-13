months = {
    "january" : 1,
    "february" : 2,
    "march" : 3,
    "april" : 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12}

def main():
    x += True
    while x == True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                m, d, y = date.split("/")  # Split date
            elif ", " in date:
                date = date.replace(",","")
                m, d, y = date.split()  # Split date

            if not m.isdigit():  # Check if month is a number
                if m.lower() in months:  # Check if month is a name
                    m = months.get(m.lower())  # Get month number
                else:
                    print("Invalid date")
            if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:   # Validate month and day
                date = f"{str(y)}-{str(m).zfill(2)}-{str(d).zfill(2)}"  # Format date
                m = int(m)
                y = int(y)
                d = int(d)
                print(date)
                break
            else:
                print("Invalid date")
                continue
        except ValueError:
            print("Invalid input")
            continue
        except UnboundLocalError:
            print("Invalid Unbound")
            continue


if __name__ == "__main__":
    main()
