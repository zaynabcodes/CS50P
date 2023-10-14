import re

def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    if match := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        if 0 <= int(match.group(1)) <= 255:
            if 0 <= int(match.group(2)) <= 255:
                if 0 <= int(match.group(3)) <= 255:
                    if 0 <= int(match.group(4)) <= 255:
                        return True
    return False

if __name__ == "__main__":
    main()
