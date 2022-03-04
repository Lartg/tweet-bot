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