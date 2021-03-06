import json, sys
from text_to_list import text_to_list
from markov_chain_data import markov_chain_data_nth
from text_cleanup import clean_text

def update_master_dict(dictionary):
  with open('master_dict.json', 'r') as master_dict:
    data = json.load(master_dict)
  master_dict.close()
  for key in dictionary.keys():
    data[key] = dictionary[key]
  with open('master_dict.json', 'w') as master_dict:
    master_dict.write(json.dumps(data))
  master_dict.close()


if __name__ == '__main__':
  text_file = sys.argv[1]
  text = clean_text(text_file)
  word_list = text_to_list(text)
  master_dict_data = markov_chain_data_nth(word_list, 3)
  update_master_dict(master_dict_data)