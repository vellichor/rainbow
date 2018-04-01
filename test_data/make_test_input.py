#!/usr/bin/env python
import hashlib
import random

NUM_INPUTS = 15
MAX_RECORD_ID = 100
MAX_RAW_VALUE = 10**9

def old_hash(raw_str):
	h = hashlib.md5()
	h.update(raw_str)
	return h.hexdigest()

def new_hash(raw_str):
	h = hashlib.new('ripemd160')
	h.update(raw_str)
	return h.hexdigest()

random.seed()

# open some output files
input_file = open('input_hashes.txt', 'w')
output_file = open('output_hashes.txt', 'w')
# optionally hold onto the raw set of secret numbers, so we can check our work
# secret_file = open('secret_data.txt', 'w')

for i in range(NUM_INPUTS):
	record_id = random.randrange(MAX_RECORD_ID)
	raw_value = "%09d" % random.randrange(MAX_RAW_VALUE)
	old_hashed = old_hash(raw_value)
	new_hashed = new_hash(raw_value)

	print >> input_file, "%s,%s" % (record_id,old_hashed)
	print >> output_file, "%s,%s" % (record_id,new_hashed)
#	print >> secret_file, "%s,%s" % (record_id,raw_value)

input_file.close()
output_file.close()
#secret_file.close()
