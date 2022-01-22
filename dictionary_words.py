import random, sys

corpus = open('/usr/share/dict/words', 'r')
dictionary = corpus.readlines()
corpus.close()

words = []

if __name__ == '__main__':
  number = int(sys.argv[1]) or random.randint(len(dictionary)-1)
  
  for x in range(number):
    index = random.randint(0, len(dictionary)-1)
    word = dictionary[index].strip('\n')
    words.append(word)

  print(*words, ' ')