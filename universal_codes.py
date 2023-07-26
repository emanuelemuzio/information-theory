import math
import matplotlib.pyplot as plt
import random

# Write a program in a programming language of your choice that computes all the
# universal codes of integers we have studied (encoding and decoding).
# Plot for each n=1,..,1000 the lengths of the binary, gamma, delta, Fibonacci
# codes. Also consider the Rice encoding for k=5 and k=7.
# Report the statistics on the following experiments:
# - number of bits required to encode 100 integers between 1 and 100.000
# (consider integers 1, 1011, 2021,...)
# - number of bits required to compress 100 random integers between 1 and
# 1000
# - number of bits required to encode a sequence of 1000 integers with a
# distribution chosen in advance

#Encoding and decoding functions

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

# Get length of encoding and experiment with different pools of values

def gamma_len(integer):
    return len(gamma_encode(integer))

def delta_len(integer):
    return len(delta_encode(integer))

def fibonacci_len(integer):
    return len(fibonacci_encoding(integer))

def rice_len(integer, k):
    return len(rice_encode(integer, k))

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

#Plots

x = range(1, 1000)
k_values = [5, 7]

plt.subplot(3, 3, 1)

gamma_y = list(map(gamma_len, x))
delta_y = list(map(delta_len, x))
fibonacci_y = list(map(fibonacci_len, x))

plt.plot(x, gamma_y, label = "Gamma")
plt.plot(x, delta_y, label = "Delta")
plt.plot(x, fibonacci_y, label = "Fibonacci")

plt.legend()
plt.title('Gamma, Delta, Fibonacci')
plt.xlabel('N')
plt.ylabel('Encoding length')

plt.subplot(3, 3, 2)

for k in k_values:
    rice_y = []
    for i in x:
        rice_y.append(rice_len(i, k))
    plt.plot(x, rice_y, label = f"Rice k = {k}")
    
plt.legend()
plt.xlabel('N')
plt.title('Rice')
plt.ylabel('Encoding length')

exp_1 = list(range(1, 100000, 1010))
exp_2 = list(sorted(random.sample(range(1, 1000), 100)))
exp_3 = list(range(50, 250)) + list(range(600, 1200)) + list(range(2000, 2100)) + list(range(10000,10100)) 
    
res_1 = exp(exp_1)
res_2 = exp(exp_2)
res_3 = exp(exp_3)
print('Done')   

experiments = [exp_1, exp_2, exp_3]
results = [res_1, res_2, res_3] 

for index in range(0, len(results)):
    plt.subplot(3, 3, index + 3)

    res = results[index]

    gamma_y_exp = list(map(lambda x: x['gamma']['len'], res))
    delta_y_exp = list(map(lambda x: x['delta']['len'], res))
    fibonacci_y_exp = list(map(lambda x: x['fibonacci']['len'], res))
    rice_y_exp_5 = list(map(lambda x: x['rice_5']['len'], res))
    rice_y_exp_7 = list(map(lambda x: x['rice_7']['len'], res))

    plt.plot(experiments[index], gamma_y_exp, label = "Gamma")
    plt.plot(experiments[index], delta_y_exp, label = "Delta")
    plt.plot(experiments[index], fibonacci_y_exp, label = "Fibonacci")
    plt.plot(experiments[index], rice_y_exp_5, label = "Rice k = 5")
    plt.plot(experiments[index], rice_y_exp_7, label = "Rice k = 7")

    plt.legend()
    plt.title(f'Experiment n.{index + 1}')
    plt.xlabel('N')
    plt.ylabel('Encoding length')
    
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
plt.show()