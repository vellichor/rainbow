#!/usr/bin/env python
"""mapper_add_digit.py"""
##############################
#
# For a bunch of input values, output those values with each of [0-9] appended
#
##############################

import sys
import json

MAX_RAINBOW = 9

# input comes from STDIN (standard input)
# it's like <record_id>,<hash> or it's a raw ssn.
for line in sys.stdin:
  line = line.strip() # pick off whitespace
  for i in range(10):
    print "%s%d" % (line, i)
