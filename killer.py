#!/usr/bin/python2
import sys

def find_optimal_word(words, sequence):
  print "words are: ", words
  print "sequence is: ", sequence
  return words[0]

def main():
  if len(sys.argv) is not 2:
    print "Provide an input file"
    return
  infile = sys.argv[1]

  f = open(infile, 'r')
  testcases = int(f.readline())
  for case in range(testcases):
    print "Case #%d:" % case, 
    (num_words, num_sequences) = f.readline().split()
    words = []
    solutions = []
    for word in range(int(num_words)):
      new_word = f.readline().strip()
      words.append(new_word)
    for sequence in range(int(num_sequences)):
      this_sequence = f.readline()
      answer = find_optimal_word(words, this_sequence)
      print "%s" % answer,
    print
    

if __name__ == '__main__':
  main()
