import string

def REPAIR_encode(T):
    S = 0
    w = T

    dictionary = {}

    while True:
        symbols = set()
        
        for c in w:
            symbols.add(c)
        
        pairs = {}
        
        halt = True
        
        for i in range(0, len(w) - 1):
            #Identifico le coppie di simboli xy tali da essere la coppia di simboli più frequenti senza sovrapposizioni. Se nessuna coppia appare più di una volta, allora mi fermo
            xy = w[i] + w[i + 1]
            pairs[xy] = w.count(xy)
            if pairs[xy] > 1:
                halt = False
        
        if halt:
            break
        
        for x in symbols:
            for y in symbols:
                if (x+y) in w:
                    pairs[(x+y)] = w.count(x+y)
                                    
        keys, values = list(pairs.keys()), list(pairs.values())
        
        max_val = -1
        max_index = -1
        
        for index in range(len(values)):
            if values[index] >= max_val:
                max_val = values[index]
                max_index = index
                
        seq = keys[max_index]
        
        dictionary_symbol = string.ascii_uppercase[S]
        
        #Rimpiazzo tutte le occorrenze di xy con un nuovo simbolo

        w = w.replace(seq, dictionary_symbol)
        
        dictionary[dictionary_symbol] = seq
        
        S = S + 1
    
    return w, dictionary

#Processo inverso: a ritroso sostituisco i simboli in w

def REPAIR_decode(w, dictionary):
    for key in list(reversed(dictionary.keys())):
        w = w.replace(key, dictionary[key])
    return w

#Ottenimento grammatica CNF

def CNF(S):
    
    symbols = []
    for s in S:
        if not s in symbols:
            symbols.append(s)

    #Ottenimento regole terminali
        
    terminal = {}
    for s in symbols:
        terminal[f'F{len(terminal)}'] = s 
        
    non_terminal = {}

    #Regole non terminali
    
    for rule1 in terminal:
        for rule2 in terminal:
            if rule1 != rule2:
                if (terminal[rule1] + terminal[rule2]) in S:
                    non_terminal[f'F{len(terminal) + len(non_terminal)}'] = s 
                elif (terminal[rule2] + terminal[rule1]) in S:
                    non_terminal[f'F{len(terminal) + len(non_terminal)}'] = s 

    #Stesso processo di RE-PAIR
                    
    while True:
        symbols = set()
        
        for c in w:
            symbols.add(c)
        
        pairs = {}
        
        halt = True
        
        for i in range(0, len(w) - 1):
            xy = w[i] + w[i + 1]
            pairs[xy] = w.count(xy)
            if pairs[xy] > 1:
                halt = False
        
        if halt:
            break
        
        for x in symbols:
            for y in symbols:
                if (x+y) in w:
                    pairs[(x+y)] = w.count(x+y)
                                    
        keys, values = list(pairs.keys()), list(pairs.values())
        
        max_val = -1
        max_index = -1
        
        for index in range(len(values)):
            if values[index] >= max_val:
                max_val = values[index]
                max_index = index
                
        seq = keys[max_index]
        
        dictionary_symbol = string.ascii_uppercase[S]
        
        w = w.replace(seq, dictionary_symbol)
        
        dictionary[dictionary_symbol] = seq
        
        S = S + 1
    
    return w, dictionary
        
    
    