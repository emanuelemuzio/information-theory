import huffman

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

def get_fib_sequence(N):
    i = 1
    fib_list = [0, 1]
    
    while fib_list[i] + fib_list[i - 1] <= N:
        fib_list.append(fib_list[i] + fib_list[i - 1])
        i = i + 1
    
    return fib_list[2:]

def get_fib_number(i):
    a, b = 0, 1
    for x in range(i):
        a, b = b, a + b
    return a

def fibonacci_encoding(N):
    fib_sequence = get_fib_sequence(N)
    encoding = ['0'] * len(fib_sequence)
    
    while N > 0:
        fib_sequence = get_fib_sequence(N)
        largest_fib = max(fib_sequence)
        N = N - largest_fib
        i  = fib_sequence.index(largest_fib)
        encoding[i] = '1' 
            
    encoding.append('1')
        
    return "".join(encoding)

def fibonacci_decoding(fib_enc):
    fib_enc = list(fib_enc)[:-1]
    decoding = []
    pos = 2
    
    for bit in fib_enc:        
        if bit == '1':
            decoding.append(get_fib_number(pos))
        pos = pos + 1
    
    return decoding

integer = int(input ('Enter an integer greater than 0: \n'))

gamma_enc = gamma_encode(integer)
gamma_dec = gamma_decode(gamma_enc)
delta_enc = delta_encode(integer)
delta_dec = delta_decode(delta_enc)
fib_enc = fibonacci_encoding(integer)
fib_dec = fibonacci_decoding(fib_enc)

print(f'The gamma encoded integer is {gamma_enc}')
print(f'The gamma decoded integer is {gamma_dec}')
print(f'The delta encoded integer is {delta_enc}')
print(f'The delta decoded integer is {delta_dec}')
print(f'The Fibonacci encoded integer is {fib_enc}')
print(f'The Fibonacci decoded integer is {fib_dec}')