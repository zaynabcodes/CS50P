import csv
import sys
from tabulate import tabulate

def main():
  filename = check_arguments()
  data = read_file(filename)

  print(tabulate(data, headers="firstrow", tablefmt="grid"))

def check_arguments():
  # original argument checking code
  if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
  elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

  return sys.argv[1]

def read_file(filename):
  data = []

  with open(filename) as file:
    reader = csv.reader(file)
    for row in reader:
      data.append(row)

  return data

if __name__ == "__main__":
  main()

