#Ordino alfabeticamente tutte le permutazioni della stringa T e conservo in I l'indice di T, il risultato della codifica BWT è l'ultima colonna della "matrice" di permutazioni ottenuta e l'indice I utile alla decodifica

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

#Codifica LZ77 tramite dizionario e sliding window di una stringa : nel search buffer abbiamo la parte già codificata, nel loook-ahead quella da codificare

def LZ77_encode(T, w):
    encoding = []
    search_buffer = ''
    look_ahead_buffer = T
    
    while len(look_ahead_buffer) > 0:
        triplet, search_buffer, look_ahead_buffer = LZ77_step(search_buffer, look_ahead_buffer, w)
        encoding.append(triplet)
    return encoding
            
def boundary_check(sequence, look_ahead_buffer):
    longest_subs = []
    
    for x in range(1, len(sequence)):
        if sequence.startswith(look_ahead_buffer[:x]):
            longest_subs.append(look_ahead_buffer[:x])
        else:
            break
    
    if len(longest_subs) == 0:
        return -1
    else:
        return len(max(longest_subs, key=len))
    
#Cerchiamo la sequenza più lunga in comune tra i due buffer e costruiamo triplette (o, l, s))
# o è l'offset tra la sequenza nel search buffer e quella nel look-ahead buffer
# l è la lunghezza della sequenza
# s è il simbolo che appare nel look-ahead buffer come prefisso dopo la sequenza
            
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
        offset = len((search_buffer.split(longest_seq))[-1]) 
        o = offset + l
        
        if offset == 0:
            boundary_offset = boundary_check(longest_seq, look_ahead_buffer[l+1:])
            if boundary_offset > 0:
                l = l + boundary_offset 
        
        new_search_buffer = search_buffer + look_ahead_buffer[:l+1]
        
        if l < len(look_ahead_buffer):
            s = look_ahead_buffer[l]    
        else: 
            s = ''
        
        new_look_ahead_buffer = look_ahead_buffer[l+1:]
        
        triplet = [o, l, s] 
                
        return triplet, new_search_buffer, new_look_ahead_buffer
    
#Il processo di decodifica delle triplette è molto semplice: considerato un offset dalla fine della stringa di o, copio i successivi l caratteri e aggiungo s alla codifica
    
def LZ77_decode(lz77_enc):
    decoding = ''
    
    for o, l, s in lz77_enc:
        o_offset = len(decoding) - o
        l_offset = o_offset + l
        triplet_seq = decoding[o_offset: l_offset] + s
        boundary_seq = ''
        if l > o:
            boundary_seq = decoding[o_offset: l_offset - o]
        decoding = decoding + triplet_seq + boundary_seq
    return decoding

#Molto simile a LZ77 ma prevede coppie piuttosto che triplette: se non troviamo una corrispondenza tra i due buffer, allora avremo (0, s), in caso contrario se troviamo una sequenza ripetuta avremo una coppia con offset e lunghezza della sequenza

def LZss_encode(T, w):
    encoding = []
    search_buffer = ''
    look_ahead_buffer = T
    
    while len(look_ahead_buffer) > 0:
        pair, search_buffer, look_ahead_buffer = LZss_step(search_buffer, look_ahead_buffer, w)
        encoding.append(pair)
    return encoding

#Versione adattata all LZss dello step di codifica e ricerca sequenza più lunga tra buffer
            
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
   
#Processo di decodifica simile a quello già visto: aggiungiamo semplicemente la lettera alla fine se troviamo una coppia (0, s), in caso contrario procediamo con la copia di l lettere a partire da un offset o (o, l)

def LZss_decode(lzss_enc):
    decoding = ''
    
    for x, y in lzss_enc:
        if isinstance(y, str):
            decoding = decoding + y
        else:
            seq = decoding[-x : len(decoding) - x + y]
            decoding = decoding + seq
    return decoding

#Funzione per il conteggio delle sequenze di lettere uguali per BWT
    
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
