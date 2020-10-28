pokemon_chain = {}
file = open("pokemon_names.txt", 'r', encoding = 'utf-8')
pokemon_names = file.read().split()
for names in pokemon_names:
    if names[0] not in pokemon_chain:
        pokemon_chain[names[0]] = [names]
    else:
        pokemon_chain[names[0]].append(names)

longest_count = 0
longest_chain = []

def longest_name(chain):
    global longest_count
    global longest_chain

    # Longest checking for chain and count
    if len(chain) > longest_count:
        longest_count = len(chain)
        longest_chain = chain

    # Finding the next Pokemon suitable for the chain
    if chain[-1][-1] in pokemon_chain:
        for name in pokemon_chain[chain[-1][-1]]:
            if name not in chain:
                longest_name(chain + [name])

# Find all the longest name
for names in pokemon_names:
    longest_name([names])

# Total Chain and Length
print("Full Chain: {} length: {}".format(longest_chain, longest_count))