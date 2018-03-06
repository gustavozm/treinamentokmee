#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import re
import string

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def remove_simbolo(texto):
    return re.sub('[%s]' % re.escape(string.punctuation), "", texto or '')

def limpa_texto(texto, simbolo):
    txt = texto.replace(simbolo, ' ')
    return txt

def ler_arquivo(arq):
    f = open(arq, 'rU')
    conteudo = f.read()
    conteudo = conteudo.split()
    f.close
    coteudo = remove_simbolo(conteudo.lower)
    return conteudo

def print_words(arquivo):
    texto = ler_arquivo(arquivo)
    #palavras = []
    #palavras_iguais = []
    dic_palavras = {}

    for palavras in texto:
        palavra =palavra.lower
        if dic_palavras.get(palavra):
            dic_palavras[palavra] += 1
        else:
            dic_palavras[palavra] = 1

    for key, count in sorted(dic_palavras.itens(), key=lambda x: x[1]):
        print key, count

    """ 
    for i in palavras:
        if plv <> i:
            plv = i
            palavras_iguais.append(i)
            conta += 1
            dic_palavras [i] = conta 
        else:
            plv = i
            conta = 0
    conta = 0
    for ii in palavras_iguais:
        conta += 1
    """
    print dic_palavras
    return dic_palavras


def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()

