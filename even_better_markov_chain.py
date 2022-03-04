import json
import random

char_limit = random.randint(100,225)
tweet = ''

with open('master_dict.json', 'r') as master_dict:
  data = json.load(master_dict)
master_dict.close()


key = random.choice(list(data.keys()))
tweet += f'{key}'
while len(tweet) <= char_limit:
  check = False
  while check == False:
    word_list = data[key]
    split_key = key.split()
    new_word = random.choice(word_list)
    split_key.pop(0)
    split_key.append(f'{new_word}')
    potential_key = ''
    for word in split_key:
      potential_key += f' {word}'
    
    
    
    key = potential_key[1:]
    check = True
  
  tweet += f' {new_word}'
  

print(f'{tweet}.')

