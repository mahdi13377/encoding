unicode_range = 0x10000 

def decode(string):
    alphabet = ''.join(chr(i) for i in range(unicode_range))
    parts = [string[i:i+2] for i in range(0, len(string), 2)]
    if parts[-1].endswith('='):
        parts[-1] = parts[-1][:-1]

    decoded_nodes = []
    for index, node in enumerate(parts):
        reversed_node = ""
        for character in node:
            if character in alphabet:
                new_index = (alphabet.index(character) - index) % len(alphabet)
                reversed_node += alphabet[new_index]
            else:
                reversed_node += character
        decoded_nodes.append(reversed_node)

    decoded_nodes = decoded_nodes[::-1]
    decoded_string = ''.join(decoded_nodes)
    return decoded_string

def encode(string):
    alphabet = ''.join(chr(i) for i in range(unicode_range))
    parts = [string[i:i+2] for i in range(0, len(string), 2)]
    
    if len(parts[-1]) == 1:
        parts[-1] += '='
    
    nodes = parts[::-1]

    nodes_a = []

    for node_index, node in enumerate(nodes):
        new_node = ""
        for character in node:
            if character in alphabet:
                new_character = alphabet[(alphabet.index(character) + node_index) % len(alphabet)]
                new_node += new_character
            else:
                new_node += character
        nodes_a.append(new_node)

    return ''.join(nodes_a)
