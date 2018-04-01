#!/usr/bin/env python
"""reducer.py"""
##############################
#
# Literally do nothing. Weirdly there's no no-op reducer packaged with Streaming.
#
##############################

import sys


# input comes from STDIN
for line in sys.stdin:
    print line, # don't add a spare newline