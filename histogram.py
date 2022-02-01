from string import punctuation


corpus = None
with open('text.txt', 'r') as c:
  corpus = c.read()

def histogram(source_text):
  histogram = []
  words = source_text.translate(str.maketrans('', '', punctuation)).lower().split()
  total_number_of_words = len(words)
  
  for word in words:
    if (word, words.count(word)) in histogram:
      pass
    else:
      histogram.append((word, words.count(word)))

  return (histogram, total_number_of_words)
    
def unique_words(histogram):
  return len(histogram)

def frequency(word, histogram):
  for histogram_word in histogram:
    if word == histogram_word[0]:
      return histogram_word[1]
  return 'Word not in text'

if __name__ == '__main__':
  print(histogram(corpus)[0])
  #print(unique_words(histogram(corpus)[0]))
  
  # print(frequency('fish', histogram(corpus)[0]))