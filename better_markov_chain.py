from listogram import Listogram
from text_to_list import text_to_list
import random
#corpus = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'two', 'fish']
corpus = text_to_list('text.txt')
char_limit = 50
tweet = ''

listogram = Listogram(corpus)
key = listogram.sample()
tweet += f'{key} '

while len(tweet) <= char_limit:
  corpus_index = 0
  word_list = []
  for same_word in corpus:
    if key == same_word and corpus_index != listogram.tokens -1:
      pointer = corpus_index + 1
      new_word = corpus[pointer]
      word_list.append(new_word)
    corpus_index += 1
  tweet += f'{random.choice(word_list)} '

print(tweet)

