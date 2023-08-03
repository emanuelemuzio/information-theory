# Portfolio: Write a program in a programming language
# of your choice that, given a string T, construct the
# grammar produced by the algorithm RE-PAIR.
# Implement also the construction of the grammar in the
# Chomsky normal form.
# Compute also the size of the grammar in both cases.

import grammar as g

T = 'aaabcaabaaabcabdabd'

w, dictionary = g.REPAIR_encode(T)
RP_dec = g.REPAIR_decode(w, dictionary)
cnf = g.CNF(T)

print(f'Text to encode: {T}')
print(f'Compressed w: {w}')
print(f'Compression dictionary: {dictionary}')
print(f'Decoded dictionary: {RP_dec}')

