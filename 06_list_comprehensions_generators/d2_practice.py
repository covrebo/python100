import random


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

# write a list comprehension to convert the names to title case
print([name.title() for name in NAMES])

# write a list comprehension to reverse the order of the names in the list
print([' '.join(reversed(name.split())) for name in NAMES])


def generate_pairs(names):
    first_names = []
    [first_names.append(str.split(name)[0]) for name in names]
    name_pairs = []
    while len(first_names) > 1:
        name1 = random.choice(first_names)
        first_names.remove(name1)
        name2 = random.choice(first_names)
        first_names.remove(name2)
        pair = (name1.title(), name2.title())
        name_pairs.append(pair)
    for pair in name_pairs:
        yield pair

pair = generate_pairs(NAMES)

for i in pair:
    print(f'{i[0]} is paired with {i[0]}')