import random, sys

strings = []

if __name__ == "__main__":
  for argument in sys.argv:
    if argument != sys.argv[0]:
      if len(strings) > 0:
        index = random.randint(0,len(strings))
      else:
        index = 0
      strings.insert(index, argument)
  print(*strings, ' ')
