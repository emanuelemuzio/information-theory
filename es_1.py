# a. Write a program in a programming language of your choice that applies Sardinas-Patterson algorithm and returns the type of code received as input.

# b. Apply the algorithm to test whether C={012, 0123, 4, 310, 1024, 2402, 2401, 4013} is UD.

# c. Apply the algorithm to verify which of the codes C1 = 10, 010, 1, 1110 , 𝐶2 = 0, 001, 101, 11 , 𝐶3 = 0, 2, 03, 011, 104, 341, 11234 , 𝐶4 = {01,10,001,100,000,111} are UD.
import sardinas_patterson as sp

C = ['012', '0123', '4', '310', '1024', '2402', '2401', '4013']
C1 = ['10','010','1','1110']
C2 = ['0','001','101','11']
C3 = ['0','2','03','011','104','341','11234']
C4 = ['01','10','001','100','000','111']

codes = [C, C1, C2, C3, C4]
    
for code in codes:
    sp.sardinas_patterson(code)
        
    
            
            
        

    