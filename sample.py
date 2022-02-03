import random
from histogram import histogram

def sample_word(histogram, word_count):
  
  selected_index = random.uniform(0,word_count)
  index = 0
  for word in histogram:
    index += word[1]
    if index >= selected_index:
      return word[0]
  return 'error'


if __name__ == "__main__":
  # test_histogram = None
  # with open('text.txt', 'r') as corpus:
  #   test_histogram = histogram(corpus.read())
  corpus = 'one fish two fish red fish blue fish'
  test_histogram = histogram(corpus)
  print(test_histogram)
  string = ''
  for x in range(100000):
    string += f" {sample_word(test_histogram[0], test_histogram[1])}"
  print(histogram(string)[0])
  pass