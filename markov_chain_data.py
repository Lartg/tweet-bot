from listogram import Listogram
from text_to_list import text_to_list
import random
# corpus = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'two', 'fish']
# corpus = text_to_list('text.txt')

#listogram = Listogram(corpus) 

# def markov_chain_data(listogram, corpus_as_list):
#   corpus = corpus_as_list
#   dictionary_of_histograms = {}
#   for word in listogram:
#     key = word[0]
#     corpus_index = 0
#     word_list = []
#     for same_word in corpus:
#       if key == same_word and corpus_index != listogram.tokens -1:
#         pointer = corpus_index + 1
#         new_word = corpus[pointer]
#         word_list.append(new_word)
#       corpus_index += 1
#     dictionary_of_histograms[key] = word_list
#   return dictionary_of_histograms

def markov_chain_data_nth(corpus_as_list, order):
  corpus = corpus_as_list
  dictionary_of_histograms = {}
  for i in range(len(corpus)-order):
    key = f'{corpus[i]}'
    for pointer in range(1,order):
      key += f' {corpus[i+pointer]}'
    if key in dictionary_of_histograms.keys():
      dictionary_of_histograms[key].append(corpus[i+order])
    else:
      if len(corpus)-1 >= i+order+1:
        dictionary_of_histograms[key] = [corpus[i+order]]
  return dictionary_of_histograms