# Write a program in a programming language of your choice given an input text
# find the Huffman encoding of the text. A decoding procedure to recover the
# original message by starting from the Huffman encoding is also required.
import huffman as h
        
if __name__ == '__main__':
    text = input("Insert the text you want to encode and then decode with Huffman's encoding: \n")
    source = h.get_source(text)
    tree = h.build_tree(source)
    encoded_text = h.huffman_encode(text, tree)
    decoded_text, decoding_table = h.huffman_decode(encoded_text, tree)
    print(f'Original text: {text}')
    print(f'Encoded text: {encoded_text}')
    print(f'Decoded text: {decoded_text}')
    print(f'Decoding table: ')
    for key in decoding_table.keys():
        print(f"{key} | {decoding_table[key]['prob']} | {decoding_table[key]['codeword']}")