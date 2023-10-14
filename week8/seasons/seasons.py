import datetime
import sys
import inflect
p = inflect.engine()
import re

class Convert:
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day

  def __str__(self):
    today = datetime.date.today() #todays date
    birth_date = datetime.date(self.year, self.month, self.day) #formats the number
    days = (today - birth_date).days #subtracts to find the amount of days since birth
    minutes = round(days * 24 * 60)
    words = p.number_to_words(minutes, andword="") #multiply to find the minutes
    return f"{words} minutes".capitalize()#converts the minutes into words, then returns


def check(birthday):
    if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birthday): #validates the users input
        #seperates values into groups
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        return Convert(year, month, day) #returns values to Convert class
    if birthday != match:
        sys.exit("Invalid format")

def main():
    birthday = input("What's your birthday in YYYY/MM/DD format? ") #gets birthday from user YYYY/MM/DD format
    result = check(birthday) #gets data from check and sets it to result
    print(result) #prints the data

if __name__ == "__main__":
    main()