import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #validates users input
    pattern = "([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + pattern + " to " + pattern + "$", s)
    if match:
        #sets starting time of users input
        start_hour = int(match.group(1)) #must be int to be able to compare in format()
        start_min = int(match.group(2)) if match.group() is None else 0 #must be int to be able to compare in format()
        start_time = match.group(3)

        #sets ending time of users input
        end_hour = int(match.group(4)) #must be int to be able to compare in format()
        end_min = int(match.group(5)) if match.group() is None else 0 #must be int to be able to compare in format()
        end_time = match.group(6)

        return format(start_hour, start_min, start_time, end_hour, end_min, end_time)

    else:
        raise ValueError

def format(start_hour, start_min, start_time, end_hour, end_min, end_time):
    if start_hour == 12:
        if "AM" in start_time:
            start_hour -= 12
    elif end_hour == 12:
        if "AM" in end_time:
            end_hour -= 12

    if "PM" in start_time:
        start_hour += 12
    elif end_hour == 12 and "PM" in end_time:
        end_hour = end_hour
    elif "PM" in end_time:
        end_hour += 12


    elif start_min == None:
        start_min = "00"
    elif end_min == None:
        end_min = "00"

    return f"{start_hour:02d}:{start_min:02d} to {end_hour:02d}:{end_min:02d}"

if __name__ == "__main__":
    main()