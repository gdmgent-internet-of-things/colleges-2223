x = 7 # integer (int)
print(f'{x} is a {type(x)}')
x = 7.5 # float (float)
print(f'{x} is a {type(x)}')
x = '7.82' # string (str)
print(f'{x} is a {type(x)}')
x = True # False (bool)
print(f'{x} is a {type(x)}')
x = [1, 2, 3, 4] # list
print(f'{x} is a {type(x)}')
x = {
    1: 'Jan',
    2: 'Feb'
} # dictionary (dict)
print(f'{x} is a {type(x)}')

# String
x = '6'
x = "6"
x = '''
Like Graphics
Love Code
Make Cool Stuff
'''
print(f'{x}')
print('Cool print stuff "{1:>09}" "{0:<09}"'.format(8, 9))

# int
x = 6

# float
x = 0.1
y = 0.3
z = x + x + x - y
print(f'{z}')

# decimal
from decimal import Decimal
x = Decimal('0.1') 
y = Decimal('0.3')
z = x + x + x - y
print(f'{z} is from type {type(z)}')

# Boolean
x = not ''
if x:
    print('x is true')
else: 
    print('x is false')

# Sequence types

# list is mutable
x = [1, 2, 3, 4, 5]
x[2] = 24
for v in x:
    print(f'v is {v}')

# tuple is immutable
x = (1, 2, 3, 4, 5)
print(f'{type(x)}')
# x[2] = 24 # does not work
for v in x:
    print(f'v is {v}')

# range is immutable
x = range(100)
# x[45] = 35
print(f'{type(x)}')
for v in x:
    print(f'v is {v}')

x = range(5, 100, 5)
for v in x:
    print(v, end=' ', flush=True)
print()

x = list(range(5, 100, 5))
x[10] = 35
for v in x:
    print(v, end=' ', flush=True)
print()

# Dictionary
x = { 1: 'one', 2: 'two', 3: 'three' }
for k in x:
    print(f'key is {k} with value {x[k]}')

x[1] = 'ten'
for k, v in x.items():
    print(f'key is {k} with value {v}')

x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print(f'id of x is {id(x)}')
print(f'id of y is {id(y)}')
if x is y:
    print('x equals y')
else:
    print('Nope')
    
# Check if variable is of a certain type
if isinstance(x, tuple):
    print('Yep')
else:
    print('Nope')

x = '5'
y = '5'
print(f'id of x is {id(x)}')
print(f'id of y is {id(y)}')

