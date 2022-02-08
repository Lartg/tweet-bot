from string import punctuation
def text_to_list(file):
  with open(file, 'r') as c:
    corpus = c.read()
    words = corpus.translate(str.maketrans('', '', punctuation)).lower().split()
    return words
