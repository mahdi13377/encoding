import sys

string = ''.join(sys.argv[1:])

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def split_into_nodes(s):
    parts = [s[i:i+2] for i in range(0, len(s), 2)]
    
    if parts[-1].endswith('='):
        parts[-1] = parts[-1][:-1]
    
    return parts

def reverse_shift(node, shift):
    reversed_node = ""
    for character in node:
        if character in alphabet:
            new_index = (alphabet.index(character) - shift) % len(alphabet)
            reversed_node += alphabet[new_index]
        else:
            reversed_node += character
    return reversed_node

nodes = split_into_nodes(string)

decoded_nodes = []

for index, node in enumerate(nodes):
    decoded_node = reverse_shift(node, index)
    decoded_nodes.append(decoded_node)

decoded_nodes = decoded_nodes[::-1]
decoded_string = ''.join(decoded_nodes)
print(decoded_string)
