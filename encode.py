import sys

string = ''.join(sys.argv[1:])

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def nodify(s):
    parts = [s[i:i+2] for i in range(0, len(s), 2)]
    
    if len(parts[-1]) == 1:
        parts[-1] += '='
    
    return parts[::-1]

nodes = nodify(string)

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

print(''.join(nodes_a))