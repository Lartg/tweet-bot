import re
import sys

def clean_text(text_file):
  with open(text_file, 'r') as text:
    corpus = text.read()
  smart_quote_pattern = '[\u201C\u201D\u201E\u201F\u2033\u2036]'
  corpus = re.sub(smart_quote_pattern, '"', corpus)
  corpus = re.sub('[.()"]', '', corpus)
  corpus = re.sub('--', ' ', corpus)
  corpus = corpus.lower()
  return corpus

if __name__ == '__main__':
  #text_file = sys.argv[1]
  text_file = 'test_text.txt'
  clean_text(text_file)