def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6: #checks if s is greater than or equal to 2 or less than or equal to 6
        for c in s: #loops through s
            if not s.isalnum(): #if s is not alnum then break out of loop
                return False

            # test for beginning two letters in s
            if s[0:2].isalpha():
                # verifies if middle of s doesn't have any numbers or 0
                middle_of_s = s[1:-1]
                if middle_of_s.isnumeric() and middle_of_s.find(0):
                    break

                zeroIndex = s.find("0") - 1

                if s[-(zeroIndex)].isdigit():
                    for x in s:
                        if x.isdigit():
                            if x.startswith('0'):
                                return False
                            else:
                                return True

                if s[-2].isdigit() and s[-1].isalpha():
                    break
                elif s[-2].isdigit():
                    return True
                elif s.isalpha():
                    return True
    else:
        return False

if __name__ == "__main__":
    main()


