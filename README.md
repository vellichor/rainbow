# Rainbow unicorn attack!

Proof of concept for a rainbow rehasher

This code is ready to run on EMR but I'm not going to document how to do that because AWS already did.

Use mapper_add_digit.py and no_op_reducer.py to build up an arbitrarily long set of n-digit numbers for your rainbow keys (numeric only)

Use mapper.py and reducer.py to rehash some dataz