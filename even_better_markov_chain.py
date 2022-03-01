import json
import random

char_limit = random.randint(50,100)
tweet = ''

with open('master_dict.json', 'r') as master_dict:
  data = json.load(master_dict)
master_dict.close()


key = random.choice(list(data.keys()))

while len(tweet) <= char_limit:
  tweet += f' {key}'
  word_list = data[key]
  key = random.choice(word_list)
  

print(tweet)

