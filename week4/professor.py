import random


def main():
  level = get_level()

  score = 0
  attempts = 0

  for _ in range(10):
    x = generate_integer(level)
    y = generate_integer(level)
    answer = x + y

    while attempts < 3:
      try:
        user_answer = int(input(f"{x} + {y} = "))

        if user_answer == answer:
            if attempts == 0:
              score += 1
              break
            else:
              attempts = 0
              break
        else:
          raise ValueError

      except ValueError:
          attempts += 1
          print("EEE")

    if attempts == 3:
      attempts = 0
      print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")
    break


def get_level():
  while True:
    try:
      level = int(input("Level: "))

      if level < 1 or level > 3:
        raise ValueError
      else:
        return level
    except ValueError:
      pass


def generate_integer(level):
  if level == 1:
    n = random.randrange(0, 9)
  if level == 2:
    n = random.randrange(10, 99)
  if level == 3:
    n = random.randrange(100, 999)

  return n


if __name__ == "__main__":
  main()