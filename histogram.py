corpus = 'one fish. two fish, red Fish blue fish'

def histogram(source_text):
  source_text = source_text.lower()
  words = source_text.split()
  histogram = []
  
  for index in range(len(words)):
    words[index] = words[index].strip('.,?!()-')

  for word in words:
    if (word, words.count(word)) in histogram:
      pass
    else:
      histogram.append((word, words.count(word)))
  return histogram
    
def unique_words(histogram):
  return(len(histogram))

def frequency(word, histogram):
  for histogram_word in histogram:
    if word == histogram_word[0]:
      return histogram_word[1]
  return 'Word not in text'

if __name__ == '__main__':
  print(histogram(corpus))
  print(unique_words(histogram(corpus)))
  print(frequency('fish', histogram(corpus)))