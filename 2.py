# Write a program in a programming language of your choice given an input text
# find the Huffman encoding of the text. A decoding procedure to recover the
# original message by starting from the Huffman encoding is also required.

class Node:
    def __init__(self, parent, left_node = None, right_node = None, value = 0, key = ''):
        self.parent = parent
        self.left_node = left_node
        self.right_node = right_node
        self.value = value
        self.key = key
        
def get_source(text : str):
    source = {}
    for i in range(len(text)):
        if not text[i] in source.keys():
            source[text[i]] = 1
        else:
            source[text[i]] = source[text[i]] + 1  
    tmp = dict(sorted(source.items(), key = lambda item: item[1], reverse = True))
    max = len(text)
    for entry in tmp:
        tmp[entry] = round(tmp[entry]/max,2)
    return tmp
        
def BFSVisit(tree):
    queue = [tree]
    
    while len(queue) > 0:
        curr = queue.pop(0)
        print(f'{curr.key} : {curr.value}')
        
        if curr.left_node is not None:
            queue.append(curr.left_node)
        
        if curr.right_node is not None:
            queue.append(curr.right_node)
            
        
def build_tree(source : str):
    nodes = []
    
    for symbol, frequency in source.items():
        node = Node(None, None, None, frequency, symbol)
        nodes.append(node)
        
    while len(nodes) > 2:
        right_node = nodes.pop()
        left_node = nodes.pop()
        parent = Node(None, left_node, right_node, left_node.value + right_node.value, f'{left_node.key},{right_node.key}')
        left_node.parent = parent
        right_node.parent = parent
        nodes.append(parent)
        nodes = sorted(nodes, key=lambda x: x.value, reverse=True)
    
    right_node = nodes.pop()
    left_node = nodes.pop()
    tree = Node(None, left_node, right_node, 1, 'Root')
    
    return tree
        
def huffman_encode(text, tree):
    encoding = ''
    
    for i in range(0, len(text)):
        codeword = search(text[i], tree)
        encoding = encoding + codeword
    
    return encoding

def huffman_decode(text, tree, source):
    decoding_table = {}
    decoding = ''
    halt = False
    
    while len(text) > 0 and not halt:
        next_bit = text[0]
        next_node = tree 
        cont = 0
        string_accumulator = ''
        
        while next_node.left_node is not None and next_node.right_node is not None and not halt:
            string_accumulator = string_accumulator + next_bit
            if next_bit == '0':
                next_node = next_node.left_node
            elif next_bit == '1':
                next_node = next_node.right_node
            cont = cont + 1
            if cont == len(text):
                halt = True
            next_bit = text[cont] if not halt else ''
        decoding = decoding + next_node.key
        if decoding_table.get(next_node.key) == None:
            decoding_table[next_node.key] = {}
            decoding_table[next_node.key]['prob'] = next_node.value
            decoding_table[next_node.key]['codeword'] = string_accumulator
        text = text[-len(text)+cont:]
        
    return decoding, decoding_table
        
def search(key, tree, string = ''):
    if key == tree.key:
        return string
    if not tree.left_node is None and key in tree.left_node.key:
        return search(key, tree.left_node, string + '0')
    if not tree.right_node is None and key in tree.right_node.key:
        return search(key, tree.right_node, string + '1')
        
if __name__ == '__main__':
    text = input("Insert the text you want to encode and then decode with Huffman's encoding: \n")
    # text = 'aeebcddegfced'
    source = get_source(text)
    tree = build_tree(source)
    # BFSVisit(tree)
    encoded_text = huffman_encode(text, tree)
    decoded_text, decoding_table = huffman_decode(encoded_text, tree, source)
    print(f'Original text: {text}')
    print(f'Encoded text: {encoded_text}')
    print(f'Decoded text: {decoded_text}')
    print(f'Decoding table: {decoding_table}')