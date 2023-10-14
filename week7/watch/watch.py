import re


def main():
  print(parse(input("HTML: ")))

def parse(s):
  if match := re.search(r'<iframe src="([^"]+)"', s): #checks if the string has "<iframe src="" with no "" and 1 or more repitions
    src = match.group(1) #sets src as the group with the link
    if 'youtube.com/embed/' in src: #checks if there is a link
      id = src.split('/embed/')[1] #splits the two, the youtube link and then the random letters/numbers and sets it to id
      return f'https://youtu.be/{id}' #returns the new link
  return None

if __name__ == "__main__":
  main()