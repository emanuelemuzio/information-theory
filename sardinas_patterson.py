# a. Write a program in a programming language of your choice that applies Sardinas-Patterson algorithm and returns the type of code received as input.

# b. Apply the algorithm to test whether C={012, 0123, 4, 310, 1024, 2402, 2401, 4013} is UD.

# c. Apply the algorithm to verify which of the codes C1 = 10, 010, 1, 1110 , 𝐶2 = 0, 001, 101, 11 , 𝐶3 = 0, 2, 03, 011, 104, 341, 11234 , 𝐶4 = {01,10,001,100,000,111} are UD.

class Halt:
    def __init__(self, halt : bool, UD : str):
        self.halt = halt
        self.UD = UD
    def __str__(self):
        return f'The algorithm halted because {self.UD}\n'
    
def check_suffix(a, b):
    if a.startswith(b):
        return a.replace(b,'',1)
    elif b.startswith(a):
        return b.replace(a,'',1)
    else:
        return ''

def intersection(a, b):
    return list(set(a) & set(b))
    

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

C = ['012', '0123', '4', '310', '1024', '2402', '2401', '4013']
C1 = ['10','010','1','1110']
C2 = ['0','001','101','11']
C3 = ['0','2','03','011','104','341','11234']
C4 = ['01','10','001','100','000','111']

codes = [C, C1, C2, C3, C4]
    
for code in codes:
        sardinas_patterson(code)
        
    
            
            
        

    