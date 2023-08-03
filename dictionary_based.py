# Write a program in a programming language of your choice, that given a text T
# outputs the LZ77 encoding and the LZss encoding of the text. 
# A paramter of the program should be W, the length of the search buffer.
# Compare the number of triplets denoted by 𝑧 produced by LZ77(T) (or by LZss) and the
# number of the equal-letter runs denoted by 𝑟 produced by the BWT(T).
import random
import string
import math
import matplotlib.pyplot as plt

def BWT_encode(T):
    permutations = []
    for i in range(0, len(T)):
        permutations.append(T[i:] + T[:i])
    
    sorted_permutations = sorted(permutations)
    
    I = sorted_permutations.index(T)
    
    word = ''
    
    for p in sorted_permutations:
        word = word + p[-1]
    return word, I    

def LZ77_encode(T, w):
    encoding = []
    search_buffer = ''
    look_ahead_buffer = T
    
    while len(look_ahead_buffer) > 0:
        triplet, search_buffer, look_ahead_buffer = LZ77_step(search_buffer, look_ahead_buffer, w)
        encoding.append(triplet)
    return encoding
            
def LZ77_step(search_buffer, look_ahead_buffer, w):
    longest_subs = []
    
    for x in range(1, len(look_ahead_buffer) + 1):
        if look_ahead_buffer[:x] in search_buffer[-w:]:
            longest_subs.append(look_ahead_buffer[:x])
        else:
            break
            
    o = 0
    l = 0
    s = look_ahead_buffer[0] 
        
    if len(longest_subs) == 0:
        triplet = [o, l, s]
        return triplet, search_buffer + look_ahead_buffer[0], look_ahead_buffer[1:]  
     
    if len(longest_subs) > 0:
        longest_seq = max(longest_subs, key=len)
        l = len(longest_seq)
        o = len((search_buffer.split(longest_seq))[-1]) + l
        new_search_buffer = search_buffer + look_ahead_buffer[:l+1]
        
        if l < len(look_ahead_buffer):
            s = look_ahead_buffer[l]    
        else: 
            s = ''
        
        new_look_ahead_buffer = look_ahead_buffer[l+1:]
        
        triplet = [o, l, s] 
                
        return triplet, new_search_buffer, new_look_ahead_buffer
    
def LZ77_decode(lz77_enc):
    decoding = ''
    
    for o, l, s in lz77_enc:
        o_offset = len(decoding) - o
        l_offset = o_offset + l
        triplet_seq = decoding[o_offset: l_offset] + s
        decoding = decoding + triplet_seq
    return decoding

def LZss_encode(T, w):
    encoding = []
    search_buffer = ''
    look_ahead_buffer = T
    
    while len(look_ahead_buffer) > 0:
        pair, search_buffer, look_ahead_buffer = LZss_step(search_buffer, look_ahead_buffer, w)
        encoding.append(pair)
    return encoding
            
def LZss_step(search_buffer, look_ahead_buffer, w):
    longest_subs = []
    
    for x in range(1, min(w, len(look_ahead_buffer)) + 1):
        if look_ahead_buffer[0:x] in search_buffer[-w:]:
            longest_subs.append(look_ahead_buffer[0:x])
        else:
            break
            
    o = 0
    l = 0
    s = look_ahead_buffer[0] 
        
    if len(longest_subs) == 0:
        pair = [o, s]
        return pair, search_buffer + look_ahead_buffer[0], look_ahead_buffer[1:]  
     
    if len(longest_subs) > 0:
        longest_seq = max(longest_subs, key=len)
        l = len(longest_seq)
        o = len((search_buffer.split(longest_seq))[-1]) + l
        new_search_buffer = search_buffer + look_ahead_buffer[:l]
        
        new_look_ahead_buffer = look_ahead_buffer[l:]
        
        pair = [o, l] 
                
        return pair, new_search_buffer, new_look_ahead_buffer
   
def LZss_decode(lzss_enc):
    decoding = ''
    
    for x, y in lzss_enc:
        if isinstance(y, str):
            decoding = decoding + y
        else:
            seq = decoding[-x : len(decoding) - x + y]
            decoding = decoding + seq
    return decoding
    
def equal_letter_runs(T):
    runs = []
    for i in range(len(T) - 1):
        cont = 1
        add = False
        for j in range(i + 1, len(T)):
            if T[i] == T[j]:
                add = True
                cont = cont + 1
            if T[i] != T[j]:
                break
        if add:
            runs.append(T[i] * cont)    
        i = j + 1  
    return runs 

w = random.randint(5, 10)

z_lz77 = []
z_lzss = []
r = []

N_range = range(5, 100)

for x in N_range:
    T = ''.join(random.choices(string.ascii_uppercase, k=x))
    z_lz77.append(len(LZ77_encode(T, w)))
    z_lzss.append(len(LZss_encode(T, w)))
    r.append(len(equal_letter_runs(T)))

plt.subplot(1, 1, 1)    
plt.plot(N_range, z_lz77, label = "LZ77")
plt.plot(N_range, z_lzss, label = "LZSS")
plt.plot(N_range, r, label = "BWT")
plt.legend()
plt.title('LZ77, LZSS, BWT')
plt.xlabel('N')
plt.ylabel('Length')
plt.show()