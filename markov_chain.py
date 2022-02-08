from listogram import Listogram
from text_to_list import text_to_list
import random
#corpus = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'two', 'fish']
corpus = text_to_list('text.txt')

listogram = Listogram(corpus) 

# given listogram creates dictionary of histograms for markov chaining

dictionary_of_histograms = {}
for word in listogram:
  key = word[0]
  corpus_index = 0
  word_list = []
  for same_word in corpus:
    if key == same_word and corpus_index != listogram.tokens -1:
      pointer = corpus_index + 1
      new_word = corpus[pointer]
      word_list.append(new_word)
    corpus_index += 1
  new_listogram = Listogram(word_list)


# make markov chain using rand char and dictionary
char_limit = random.randint(50,130)
tweet = ''
key = listogram.sample()

running = True
while running:
  tweet += f'{key} '
  
  key = random.choice(dictionary_of_histograms[key])
  if len(tweet) >= char_limit:
    running = False

print(tweet)


