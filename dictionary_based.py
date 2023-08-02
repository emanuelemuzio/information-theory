# Write a program in a programming language of your choice, that given a text T
# outputs the LZ77 encoding and the LZss encoding of the text. 
# A paramter of the program should be W, the length of the search buffer.
# Compare the number of triplets denoted by 𝑧 produced by LZ77(T) (or by LZss) and the
# number of the equal-letter runs denoted by 𝑟 produced by the BWT(T).

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
        if look_ahead_buffer[:x] in search_buffer:
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
        new_search_buffer = search_buffer + look_ahead_buffer[:l+1]
        
        if l < len(look_ahead_buffer):
            s = look_ahead_buffer[l]    
        else: 
            s = ''
        
        new_look_ahead_buffer = look_ahead_buffer[l+1:]
        
        pair = [o, l] 
                
        return pair, new_search_buffer, new_look_ahead_buffer
   
def LZss_decode(lzss_enc):
    decoding = ''
    
    for x, y in lzss_enc:
        if isinstance(y, str):
            decoding = decoding + y
        else:
            decoding = decoding + decoding[-x : -x+y]
    return decoding
    
T = ['babbababbaabbaabaabaaa','aabbabab']
w = len(T)

lz77_enc = LZ77_encode(T[-1], w)
lz77_dec = LZ77_decode(lz77_enc)
lzss_enc = LZss_encode(T[-1], w)
lzss_dec = LZss_decode(lzss_enc)

print(f'Text to encode: {T}\n')
print(f'Seach buffer dimension: {w}\n')
print(f'LZ77 Encoded text: {lz77_enc}\n')
print(f'LZ77 Decoded text: {lz77_dec}\n')
print(f'LZssEncoded text: {lzss_enc}\n')
print(f'LZss Decoded text: {lzss_dec}\n')
