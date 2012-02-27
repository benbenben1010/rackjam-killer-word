#!/usr/bin/python2

import unittest
from killer import *

class Test_Killer(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_is_word_still_eligible(self):
    known = '*b*'
    eligible_word = 'aba'
    noneligible_word = 'bab'

    self.assertTrue(is_word_still_eligible(known, eligible_word))
    self.assertFalse(is_word_still_eligible(known, noneligible_word))


if __name__ == '__main__':
  unittest.main()
