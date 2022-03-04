import re
import sys



def clean_text(text_file):
  with open(text_file, 'r') as text:
    corpus = text.read()
    
  pass

if __name__ == '__main__':
  #text_file = sys.argv[1]
  text_file = 'test_text.txt'
  clean_text(text_file)