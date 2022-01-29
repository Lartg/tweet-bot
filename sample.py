import random
from histogram import histogram

corpus = 'one fish. two fish, red Fish blue fish'

def sample_word(histogram):
  selected_index_range = 0
  for word in histogram:
    selected_index_range += word[1]
  selected_index = random.uniform(0,selected_index_range)
  index = 0
  for word in histogram:
    index += word[1]
    if index >= selected_index:
      return word[0]
  return 'error'


if __name__ == "__main__":
  string = ''
  for x in range(10000):
    string += f' {sample_word(histogram(corpus))}'
  print(histogram(string))
  pass