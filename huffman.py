#Classe helper nodo per la creazione dell'albero di codifica

class Node:
    def __init__(self, parent, left_node = None, right_node = None, value = 0, key = ''):
        self.parent = parent
        self.left_node = left_node
        self.right_node = right_node
        self.value = value
        self.key = key

#Funzione per l'ottenimento di sorgente e probabilità associata a ciascun elemento dell'alfabeto, quest'ultimo ordinato in modo decrescente        

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

#Costruzione dell'albero a partire dall'alfabeto sorgente
        
def build_tree(source : str):
    nodes = []
    
    for symbol, frequency in source.items():
        #Creo i nodi contenenti solo l'info su simbolo e sua frequenza
        node = Node(None, None, None, frequency, symbol)
        nodes.append(node)
        
    while len(nodes) > 2:
        #Il dizionario è già ordinato, per cui posso semplicemente andare a fare .pop() sui primi due elementi, sapendo che il primo sarà il maggiore e quindi il nodo destro
        right_node = nodes.pop()
        left_node = nodes.pop()
        
        #Creazione nodo padre 
        parent = Node(None, left_node, right_node, left_node.value + right_node.value, f'{left_node.key},{right_node.key}')
        left_node.parent = parent
        right_node.parent = parent
        nodes.append(parent)
        
        #Aggiorno la lista di nodi
        nodes = sorted(nodes, key=lambda x: x.value, reverse=True)
    
    right_node = nodes.pop()
    left_node = nodes.pop()
    tree = Node(None, left_node, right_node, 1, 'Root')
    
    return tree
        
#Una volta ottenuto l'albero di codifica, semplicemente vado a codificare ogni lettera del testo originale, che a questo punto sarà rappresentata dal "percorso" per raggiungere il nodo che contiene il suo simbolo

def huffman_encode(text, tree):
    encoding = ''
    
    for i in range(0, len(text)):
        codeword = search(text[i], tree)
        encoding = encoding + codeword
    
    return encoding

#A 

def huffman_decode(text, tree):
    decoding_table = {}
    decoding = ''
    halt = False
    
    #Scorro il testo codificato cercando corrispondenze nell'albero fino a trovare una foglia, continuo finchè non ho 'esaurito' la stringa codificata

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
        
#Funzione ricorsiva per la ricerca di una chiave nell'albero

def search(key, tree, string = ''):
    if key == tree.key:
        return string
    if not tree.left_node is None and key in tree.left_node.key:
        return search(key, tree.left_node, string + '0')
    if not tree.right_node is None and key in tree.right_node.key:
        return search(key, tree.right_node, string + '1')