#!/usr/bin/env python
"""reducer.py"""
##############################
#
# Second half of re-hasher.
# Input will be sorted by OLD hashed value
# There will be at least one line for all possible hashed values
# plus an extra line with a record id for any that we
# actually had in the target set.
#
# Output will have the record id with the new hashed value.
#
##############################

from operator import itemgetter
import sys
import json
import hashlib

# this will be the old hash value. 
# we check this to see when it's time to emit.
last_key = None 
output_value_dict = {}

def new_hash(raw_str):
    # TODO: do that new thing you do
    h = hashlib.new('ripemd160')
    h.update(raw_str)
    return h.hexdigest()


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    key, value = map(lambda x: x.strip(), line.split('\t', 1))
    # have we hit a key boundary? if so, time to try to generate output.
    if last_key is not None and key != last_key:
        # key boundary.
        if 'new_hashed' not in output_value_dict:
            print "That's weird, never saw a raw value for old hash value %s" % key
        elif 'record_id' in output_value_dict:
            print json.dumps(output_value_dict)
        # clear the cached data.
        output_value_dict = {}
    last_key = key
    value_dict = json.loads(value)
    if 'record_id' in value_dict:
        output_value_dict['record_id'] = record_id = value_dict['record_id']
    elif 'raw' in value_dict:
        output_value_dict['new_hashed'] = new_hash(value_dict['raw'])

# out of keys; print the last one.
if 'new_hashed' not in output_value_dict:
    print "That's weird, never saw a raw value for old hash value %s" % key
elif 'record_id' in output_value_dict:
    print json.dumps(output_value_dict)
