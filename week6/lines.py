import sys

def main():
    check_args(sys.argv)
    lines = read_lines(sys.argv[1])
    print(count_lines(lines))

#checks the arguments inputted
def check_args(arg):
    if len(arg) < 2: #checks if arg is greater than 2
        sys.exit("Too few command-line arguments")
    if len(arg) > 2: #checks if arg is less than 2
        sys.exit("Too many command-line arguments")
    if ".py" not in arg[1]: #checks if arg includes .py
        sys.exit("Not a Python file")
    return True #else returns true

# reads each line
def read_lines(arg):
    try:
        with open(arg) as file: #opens file inputted in arg
            lines = file.readlines() #reads through each lines
    except FileNotFoundError: #handles if a file doesn't exist
        sys.exit("File does not exist")
    return lines # if everything correct return true



# count the lines
def count_lines(lines):
    count = 0
    for line in lines: #iterates though lines in the read_lines(arg)
       line = line.strip() #stips each line from whitespace to remove all blank lines
       if len(line) > 0: #checks if each line is now greater than 0
           if line[0] != "#": #checks if the line doesn't have #
                count += 1 #counts it as a line and adds 1 to the count list
    return count #after all lines are checked, returns the count


if __name__ == "__main__":
    main()