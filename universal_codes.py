import huffman

integer = int(input ('Enter an integer greater than 0: \n'))

def find_exp(integer):
    N = 0
    
    while (2 ** (N + 1)) <= integer:
        N = N + 1
        
    return N

def gamma_encode(integer):

    if integer > 0:
        N = find_exp(integer)
        
        encoding = '0' * N + format(integer, 'b')
                
        return encoding
        
def gamma_decode(encoded_integer):
    N = 0
    i = 0
    
    while encoded_integer[i] == '0':
        N = N + 1
        i = i + 1
    
    decoding = int(encoded_integer[N:], 2)
    
    return decoding

def delta_encode(integer):
    N = find_exp(integer)
    encoding = gamma_encode(N + 1) + format(integer, 'b')[1:]
    return encoding

def delta_decode(encoding):
    L = 0
    i = 0
    
    while encoding[i] == '0':
        L = L + 1
        i = i + 1
    
    N = int(encoding[L : L + L + 1], 2) - 1
    
    decoding = int('1' + encoding[L + L + 1 : L + L + 1 + N], 2)
        
    return decoding

gamma_enc = gamma_encode(integer)
gamma_dec = gamma_decode(gamma_enc)
delta_enc = delta_encode(integer)
delta_dec = delta_decode(delta_enc)

print(f'The gamma encoded integer is {gamma_enc}')
print(f'The gamma decoded integer is {gamma_dec}')
print(f'The delta encoded integer is {delta_enc}')
print(f'The delta decoded integer is {delta_dec}')
