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

import integer_encoding as ie

x = range(1, 1000)

plt.subplot(3, 3, 1)

gamma_y = list(map(ie.gamma_len, x))
delta_y = list(map(ie.delta_len, x))
fibonacci_y = list(map(ie.fibonacci_len, x))

plt.plot(x, gamma_y, label = "Gamma")
plt.plot(x, delta_y, label = "Delta")
plt.plot(x, fibonacci_y, label = "Fibonacci")

plt.legend()
plt.title('Gamma, Delta, Fibonacci')
plt.xlabel('N')
plt.ylabel('Encoding length')

plt.subplot(3, 3, 2)

for k in ie.k_values:
    rice_y = []
    for i in x:
        rice_y.append(ie.rice_len(i, k))
    plt.plot(x, rice_y, label = f"Rice k = {k}")
    
plt.legend()
plt.xlabel('N')
plt.title('Rice')
plt.ylabel('Encoding length')

exp_1 = list(range(1, 100000, 1010))
exp_2 = list(sorted(random.sample(range(1, 1000), 100)))
exp_3 = list(range(50, 250)) + list(range(600, 1200)) + list(range(2000, 2100)) + list(range(10000,10100)) 
    
res_1 = ie.exp(exp_1)
res_2 = ie.exp(exp_2)
res_3 = ie.exp(exp_3)

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

print(1)