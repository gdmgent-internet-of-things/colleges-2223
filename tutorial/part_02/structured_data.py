# list is a sequence ans is mutable
x = [1, 2, 3]

# tuple is immutable
x = (1, 2, 3)

# dictonary is a sequence of key / value pairs
x = {'a': 1, 'b': 2, 'c': 3}

# set is an unordend list of unique values
x = {1, 2, 3}

# game as a list
game = ['rock', 'paper', 'scissors', 'lizard', 'spock']

# tuple is the same as a list but it is immutable
# game = ('rock', 'paper', 'scissors', 'lizard', 'spock') # append, insert, pop ... will not work => Error

# animals as a dictionary
animals = {'kitten': 'meoow', 'puppy': 'ruff', 'lion': 'grrr', 'dragon': 'rawr'}
animals = dict(kitten = 'meoow', puppy = 'ruff', lion = 'grrr', dragon = 'rawr')

# set
a = set('We are gonna need a bigger boat.')
b = set('I am sorry Dave. I am afraid I can\'t do that.')

def print_list(list):
    for item in list:
        print(item, end = ' ', flush=True)
    print()

def print_dict(dict):
    for k in dict:
        print(f'{k}: {dict[k]}')

def print_dict_to(dict):
    for k, v in dict.items():
        print(f'{k}: {v}')

def print_set(set):
    print('{', end = '')
    for c in set:
        print(c, end = '')
    print('}')

def main():
    print(game[len(game) - 1])
    print(game[game.index('lizard')])
    game.append('computer')
    game.insert(0, 'atom')
    game.remove('paper')
    del game[1:3]
    x = game.pop()
    print_list(game)
    print(', '.join(game))

    print_dict(animals)
    print_dict_to(animals)
    print(animals['lion'])
    animals['monkey'] = 'haha'
    print('found' if 'lions' in animals else 'nope')
    v = animals.get('philippe')
    print(v)

    print_set(sorted(a))
    print_set(b)
    print_set(a - b) # members of a not in set b
    print_set(a | b) # members in a or b and both
    print_set(a ^ b) # members in a or b but not both
    print_set(a & b) # members in a and b

    # Comprehension
    seq = range(23)
    print_list(seq)
    seq2 = [x * 2 for x in seq]
    print_list(seq2)
    seq2 = [x for x in seq if x % 3 != 0]
    print_list(seq2)
    seq2 = [(x, x**2) for x in seq]
    print_list(seq2)

    from math import pi
    seq2 = [round(pi, i) for i in seq]
    print_list(seq2)

    seq2 = {x: x**2 for x in seq}
    print_dict(seq2)

    seq2 = {x for x in 'superduper' if x not in 'pd'}
    print(seq2)

if __name__ == '__main__': main()