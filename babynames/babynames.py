#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def pega_ano(linha):
     ano = ''
     txtr = re.search(r'<h3\s\w+="center">P\w+\sin\s\d\d\d\d',linha)
     if txtr:
         txt1 = txtr.group()
         txtr = re.search(r'P\w+\sin\s\d\d\d\d',txt1)
         if txtr:
             txt2 = txtr.group()
             txtr = re.search(r'\d\d\d\d',txt2)
             if txtr:
                 ano = txtr.group()
     return ano

def pega_rank(linha):
    dic = []
    dic = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', linha)
    return dic

def extract_names(filename):
   #"""
   #Given a file name for baby.html, returns a list starting with the year string
   #followed by the name-rank strings in alphabetical order.
   #['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
   # """
    # +++your code here+++
    dados = []
    i = 0
    f = open(filename, 'rU')
    for linha in f:
        if pega_ano(linha):
            ano = pega_ano(linha)
            print 'Referente ao ano de '+ano

        dados = pega_rank(linha)
        if dados:
            print dados[0][0] + ' ' + dados[0][1], dados[0][0] + ' ' +  dados[0][2]
        f.next()

    f.close
    return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:
      extracao = extract_names(filename)
      if extracao:
      #    escrevar_file(extracao)
      #else:
          print extracao

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
