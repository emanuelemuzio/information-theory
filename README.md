# Teoria dell'informazione e compressione dei dati
Portfolio di esercizi per l'esame.

## Esercizi

### Es. 1

- a. Write a program in a programming language of your choice that applies Sardinas-Patterson algorithm and returns the type of code received as input.

- b. Apply the algorithm to test whether C={ 012, 0123, 4, 310, 1024, 2402, 2401, 4013 } is UD.

- c. Apply the algorithm to verify which of the codes C1 = { 10, 010, 1, 1110 }, 𝐶2 = { 0, 001, 101, 11 } , 𝐶3 = { 0, 2, 03, 011, 104, 341, 11234 } , 𝐶4 = { 01, 10, 001, 100, 000, 111 } are UD.

### Es. 2

Write a program in a programming language of your choice given an input text find the Huffman encoding of the text. 

A decoding procedure to recover the original message by starting from the Huffman encoding is also required.

### Es. 3

Write a program in a programming language of your choice that computes all the universal codes of integers we have studied (encoding and decoding).

Plot for each n=1,..,1000 the lengths of the binary, gamma, delta, Fibonacci codes. Also consider the Rice encoding for k=5 and k=7.
Report the statistics on the following experiments:
- number of bits required to encode 100 integers between 1 and 100.000 (consider integers 1, 1011, 2021,...)
- number of bits required to compress 100 random integers between 1 and 1000
- number of bits required to encode a sequence of 1000 integers with a distribution chosen in advance

Per il terzo esperimento è stata scelta una distribuzione arbitraria di valori con lo script seguente in Python:

    list(range(50, 250)) + list(range(600, 1200)) + list(range(2000, 2100)) + list(range(10000,10100)) 

Il risultato è stato il seguente insieme di grafici:

![alt text](https://github.com/emanuelemuzio/information-theory/blob/main/es_3_report_1.png?raw=true)
![alt text](https://github.com/emanuelemuzio/information-theory/blob/main/es_3_report_2.png?raw=true)
![alt text](https://github.com/emanuelemuzio/information-theory/blob/main/es_3_report_3.png?raw=true)
![alt text](https://github.com/emanuelemuzio/information-theory/blob/main/es_3_report_4.png?raw=true)

### Es. 4

Write a program in a programming language of your choice, that given a text T outputs the LZ77 encoding and the LZss encoding of the text. 

A paramter of the program should be W, the length of the search buffer.

Compare the number of triplets denoted by z produced by LZ77(T) (or by LZss) and the number of the equal-letter runs denoted by r produced by the BWT(T).

Stringa di esempio: 'babbababbaabbaabaabaaa'

![alt text](https://github.com/emanuelemuzio/information-theory/blob/main/es_4_report.png?raw=true)


### Es. 5

Write a program in a programming language of your choice that, given a string T, construct the grammar produced by the algorithm RE-PAIR.

Implement also the construction of the grammar in the Chomsky normal form.

Compute also the size of the grammar in both cases.