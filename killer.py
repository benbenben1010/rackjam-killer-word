#!/usr/bin/python2
import os, sys

def find_optimal_word(words, sequence):
  # high score = 26
  # best words = []
  # for each word in words,
  #   score_of_this_word = get_score_of_word
  #   is this score better

  print "words are: ", words
  print "sequence is: ", sequence
  return words[0]

def is_word_still_eligible(known, word):
  for index in range(len(word)):
    if known[index] is not '*' and known[index] is not word[index]:
      return False
  return True

def main():
  if len(sys.argv) is not 2:
    print "Provide an input file"
    return

  infile = sys.argv[1]
  if not os.path.exists(infile):
    print "File not found!"
    return

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
