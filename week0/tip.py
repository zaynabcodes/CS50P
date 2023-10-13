def dollars_to_float(dollars):
    dollars = dollars.replace("$","")
    return float(dollars)

def percent_to_float(percent):
    percent = percent.replace("%","")
    return float(percent)/100

def main():
    dollars_input = input("How much was the meal? ")
    dollars = dollars_to_float(dollars_input)
    percent_input = input("What percentage would you like to tip? ")
    percent = percent_to_float(percent_input)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()