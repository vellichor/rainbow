#!/usr/bin/env python
"""mapper.py"""
##############################
#
# First half of re-hasher.
# Input should include lines like <record_id>,<old hashed value>
# plus a single line for every POSSIBLE original (un-hashed) raw value
#
##############################

import sys
import json
import hashlib

def old_hash(raw_str):
  # TODO: do that thing you do
  h = hashlib.md5()
  h.update(raw_str)
  return h.hexdigest()

# input comes from STDIN (standard input)
# it's either like <record_id>,<hash> or it's a possible raw value.
for line in sys.stdin:
  # we either got a bare numeric string, or we got a tuple.
  if "," in line:
    # split and clean up some more
    record_id,old_hashed = map(lambda x: x.strip(), line.split(",", 1))
    # tab is magic; reducer will get values grouped by the stuff before the first tab.
    print "%s\t%s" % (old_hashed, json.dumps({"record_id": record_id}))
  else:
    # bare numeric string? should probably validate that, but meh.
    raw = line.strip()
    old_hashed = old_hash(raw)
    print "%s\t%s" % (old_hashed, json.dumps({"raw": raw}))