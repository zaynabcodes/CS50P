import sys
import csv

def main():
    check_args()
    read_files()

def read_files():
    try:
        with open(sys.argv[1]) as fileone:
            reader = csv.DictReader(fileone)
            data = []
            for row in reader:
                full_name = row["name"].strip('"')
                last, first = full_name.split(", ")
                house = row["house"]
                data.append({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w", newline="") as filetwo:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(filetwo, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def check_args():
    if len(sys.argv) != 3:
        sys.exit("Invalid number of command-line arguments")

if __name__ == "__main__":
    main()
