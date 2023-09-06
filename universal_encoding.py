import math

#Valori k per la codifica di Rice

k_values = [5, 7]

#Funzione per la ricerca dell'esponente N della potenza di 2 <= X

def find_exp(integer):
    N = 0
    
    while (2 ** (N + 1)) <= integer:
        N = N + 1
        
    return N

def gamma_encode(integer):

    if integer > 0:
        N = find_exp(integer)

        #La codifica prevede N '0' seguiti dalla codifica binaria di x 
        
        encoding = '0' * N + format(integer, 'b')
                
        return encoding
        
def gamma_decode(encoded_integer):
    N = 0
    i = 0
    
    while encoded_integer[i] == '0':
        N = N + 1
        i = i + 1
    
    #N = numeri di '0' prima dell'uno, decodifico in intero i successivi N + 1 bits

    decoding = int(encoded_integer[N:], 2)
    
    return decoding

#Scrivo il gamma encode di N+1 segyuti dalla rappresentazione binaria di x senza il bit più significativo

def delta_encode(integer):
    N = find_exp(integer)
    encoding = gamma_encode(N + 1) + format(integer, 'b')[1:]
    return encoding

#L = '0' fino al primo 1, recupero L + 1 bits e interpreto la sequenza come N + 1. Considero l'intero ottenuto decodificando 1 seguito dai prossimi N bits

def delta_decode(encoding):
    L = 0
    i = 0
    
    while encoding[i] == '0':
        L = L + 1
        i = i + 1
    
    N = int(encoding[L : L + L + 1], 2) - 1
    
    decoding = int('1' + encoding[L + L + 1 : L + L + 1 + N], 2)
        
    return decoding

#Funzione iterativa per il recupero della sequenza di fibonacci per l'intero N

def get_fib_sequence(N):
    i = 1
    fib_list = [0, 1]
    
    while fib_list[i] + fib_list[i - 1] <= N:
        fib_list.append(fib_list[i] + fib_list[i - 1])
        i = i + 1
    
    return fib_list[2:]

#Recupero i-esimo numero di Fibonacci

def get_fib_number(i):
    a, b = 0, 1
    for x in range(i):
        a, b = b, a + b
    return a

#Codifica di Fibonacci: sequenza di '0' lunga quanto la sequenza di Fibonacci per il numero N, se il numero di Fibonacci è l'i-esimo numero di Fib., pongo 1 in posizione i-2 e aggiungo 1 alla fine

def fibonacci_encode(N):
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

#Per la codifica rimuovo l'1 finale, assegno i valori rimasti ai bit nella codeword e sommo i valori di 1

def fibonacci_decode(fib_enc):
    fib_enc = list(fib_enc)[:-1]
    decoding = []
    pos = 2
    
    for bit in fib_enc:        
        if bit == '1':
            decoding.append(get_fib_number(pos))
        pos = pos + 1
    
    return decoding

#q = floor((x-1)/2^k), r = x-2^(k)q-1. Converto q in unario e r in binario, la codifica sarà la concatenazione di q e r

def rice_encode(integer, k):
    encodings = []
    
    q = math.floor((integer - 1) / (2 ** k)) 
    r = integer - ((2 ** k) * q) - 1
    unary_enc = '0' * q + '1' 
    binary_enc = format(r, 'b')
    binary_enc = '0' * (k - len(binary_enc)) + binary_enc
    encoding = unary_enc + binary_enc
    encodings.append(encoding)
    
    return "".join(encodings)

def gamma_len(integer):
    return len(gamma_encode(integer))

def delta_len(integer):
    return len(delta_encode(integer))

def fibonacci_len(integer):
    return len(fibonacci_encode(integer))

def rice_len(integer, k):
    return len(rice_encode(integer, k))

#Funzione helper per il plottaggio dei grafici

def exp(integers):
    
    results = []

    for i in integers:

        experiment = {}
        
        gamma  = gamma_len(i)
        experiment['gamma'] = {
            'integer' : i,
            'len' : gamma
        }
        
        delta = delta_len(i)
        experiment['delta'] = {
            'integer' : i,
            'len' : delta    
        }
        
        
        fibonacci = fibonacci_len(i)
        experiment['fibonacci'] = {
            'integer' : i,
            'len' : fibonacci
        }

        
        for k in k_values:
            k_index = f'rice_{k}'
            rice = rice_len(i, k)
            
            experiment[k_index] = {
                'integer' : i,
                'len' : rice
            }
        
        results.append(experiment)
    return results