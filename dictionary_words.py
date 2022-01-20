import random, sys

corpus = open('/usr/share/dict/words', 'r')
dictionary = corpus.readlines()
words = []

for x in range(int(sys.argv[1])):
  index = random.randint(0, len(dictionary)-1)
  word = dictionary[index].strip('\n')
  words.append(word)



print(*words, ' ')