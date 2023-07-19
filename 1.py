# a. Write a program in a programming language of your choice that applies Sardinas-Patterson algorithm and returns the type of code received as input.

# b. Apply the algorithm to test whether C={012, 0123, 4, 310, 1024, 2402, 2401, 4013} is UD.

# c. Apply the algorithm to verify which of the codes C1 = 10, 010, 1, 1110 , 𝐶2 = 0, 001, 101, 11 , 𝐶3 = 0, 2, 03, 011, 104, 341, 11234 , 𝐶4 = {01,10,001,100,000,111} are UD.

class Halt:
    def __init__(self, halt : bool, UD : str):
        self.halt = halt
        self.UD = UD
    def __str__(self):
        return f'The algorithm halted. {self.UD}'
    
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
        return Halt(True, 'The code is UD')
    if len(intersec) > 0:
        return Halt(True, 'The code is not UD')
    if len(si) == 0:
        return Halt(True, 'The code is UD')
    for j in range(0, len(s)):
        if sorted(si) == sorted(s[j]):
            return Halt(True, 'The code is UD')
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
    print(s)
    print(halting)
    print("")

C = ['012', '0123', '4', '310', '1024', '2402', '2401', '4013']
C1 = ['10','010','1','1110']
C2 = ['0','001','101','11']
C3 = ['0','2','03','011','104','341','11234']
C4 = ['01','10','001','100','000','111']

def print_menu():
    
    C_option = ", ".join(C)
    C1_option = ", ".join(C1)
    C2_option = ", ".join(C2)
    C3_option = ", ".join(C3)
    C4_option = ", ".join(C4)
    
    print(f"1. Test [{C_option}] ")
    print(f"2. Test [{C1_option}]")
    print(f"3. Test [{C2_option}]")
    print(f"4. Test [{C3_option}]")
    print(f"5. Test [{C4_option}]")
    print("6. Exit")

if __name__ == '__main__':
    options = [C, C1, C2, C3, C4]
    
    loop = True

    while loop:
        print_menu()
        
        print("")
        choice = int(input("Enter your choice [1-6]: \n"))
        print("")
        
        if choice in range(1, len(options)):
            sardinas_patterson(options[choice - 1])
        elif choice == (len(options) + 1):
            loop = False
            print('Exiting...')
        elif not choice in range(1, len(options)):
            print("Wrong menu selection, try again")
        
    
            
            
        

    