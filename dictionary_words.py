import random, sys

def random_words(text_file, num_words):
  corpus = open(text_file, 'r')
  dictionary = corpus.readlines()
  corpus.close()
  words = []
  number = num_words
  
  for x in range(number):
    index = random.randint(0, len(dictionary)-1)
    word = dictionary[index].strip('\n')
    words.append(word)

  return print(*words, ' ')



if __name__ == '__main__':
  random_words('/usr/share/dict/words', int(sys.argv[1]) or random.randint(20))