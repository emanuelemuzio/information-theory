import random
import string
import matplotlib.pyplot as plt
import dictionary_encoding as de

# Write a program in a programming language of your choice, that given a text T
# outputs the LZ77 encoding and the LZss encoding of the text. 
# A paramter of the program should be W, the length of the search buffer.
# Compare the number of triplets denoted by 𝑧 produced by LZ77(T) (or by LZss) and the
# number of the equal-letter runs denoted by 𝑟 produced by the BWT(T).

T = 'babbababbaabbaabaabaaa'
w = random.randint(5, 10)

print(de.LZss_decode(de.LZss_encode(T, w)))


z_lz77 = []
z_lzss = []
r = []

N_range = range(5, 100)

for x in N_range:
    T = ''.join(random.choices(string.ascii_uppercase, k=x))
    z_lz77.append(len(de.LZ77_encode(T, w)))
    z_lzss.append(len(de.LZss_encode(T, w)))
    r.append(len(de.equal_letter_runs(T)))

plt.subplot(1, 1, 1)    
plt.plot(N_range, z_lz77, label = "LZ77")
plt.plot(N_range, z_lzss, label = "LZSS")
plt.plot(N_range, r, label = "BWT")
plt.legend()
plt.title('LZ77, LZSS, BWT')
plt.xlabel('N')
plt.ylabel('Length')
plt.show()