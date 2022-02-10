import json, sys
from text_to_list import text_to_list
from listogram import Listogram
from markov_chain_data import markov_chain_data

corpus = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'two', 'fish']
def update_master_dict(dictionary):
  with open('master_dict.json', 'r') as master_dict:
    data = json.load(master_dict)
  master_dict.close()

  for key in dictionary.keys():
    new_entries = []
    for name in data.keys():
      if key == name:
        data[name].append(dictionary[key])
      else:
        new_entries.append(key)
    for new_entry in new_entries:
      data[new_entry] = dictionary[new_entry]

  with open('master_dict.json', 'w') as master_dict:
    master_dict.write(json.dumps(data))
  master_dict.close()


if __name__ == '__main__':
  text_file = sys.argv[1]
  word_list = text_to_list(text_file)
  listogram = Listogram(word_list)
  #listogram = Listogram(corpus)
  master_dict_data = markov_chain_data(listogram, word_list)
  
  update_master_dict(master_dict_data)


    