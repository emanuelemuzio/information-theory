#Classe per decidere se l'algoritmo deve continuare o procedere e, in caso di fermata, conservazione dell'esito

class Halt:
    def __init__(self, halt : bool, UD : str):
        self.halt = halt
        self.UD = UD
    def __str__(self):
        return f'The algorithm halted because {self.UD}\n'
    
#Ottengo tutti i suffissi w tali che a = bw o b = aw, con a e b codeword da s0 e dall'i-esimo insieme di suffissi considerato

def check_suffix(a, b):
    if a.startswith(b):
        return a.replace(b,'',1)
    elif b.startswith(a):
        return b.replace(a,'',1)
    else:
        return ''

#Controllo per uno dei tre criteri di fermata

def intersection(a, b):
    return list(set(a) & set(b))
    
#Verifica dei tre criteri di fermata dell'algoritmo: l'i-esimo insieme di suffissi è vuoto, c'è un elemento in comune tra s0 e l'ultimo insieme trovato, s0 e si sono identici

def halt(s, s0, si):
    intersec = intersection(s0, si)
    
    if len(si) == 0:
        return Halt(True, 'the last set is empty, the code is UD')
    if len(intersec) > 0:
        return Halt(True, f'the last set has an element in common with the code set, the code is not UD')
    for j in range(0, len(s)):
        if sorted(si) == sorted(s[j]):
            return Halt(True, f'the last set and the {j + 1}-th are equal, the code is UD')
    return Halt(False, '')
    
    
def sardinas_patterson(code : list):
    s = [code]
    suffixes = []
    halting = Halt(False, '')
    i = 0
    while not halting.halt:
        i = i + 1       
        s.append([])
        for a in s[0]:
            for b in s[i - 1]:
                w = check_suffix(a, b)
                if len(w) > 0 and w not in s[i]: 
                    s[i].append(w)
        halting = halt(suffixes, s[0], s[i])
        suffixes.append(s[i])
        
    print(f'The code is:\n{s[0]}')
    for i in range(1, len(s)):
        print(s[i])
    print(halting)