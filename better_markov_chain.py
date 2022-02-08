from listogram import Listogram
from text_to_list import text_to_list
import random
corpus = text_to_list('text.txt')
char_limit = random.randint(50,100)
tweet = ''
corpus_length = len(corpus)
listogram = Listogram(corpus)
key = random.choice(corpus)
tweet += f'{key} '
while len(tweet) <= char_limit:
  word_list = []
  for index, same_word in enumerate(corpus):
    if key == same_word and index != corpus_length-1:
      pointer = index + 1
      new_word = corpus[pointer]
      word_list.append(new_word)
  potential_key = random.choice(word_list)
  
  key = potential_key
  tweet += f'{key} '

print(tweet)

