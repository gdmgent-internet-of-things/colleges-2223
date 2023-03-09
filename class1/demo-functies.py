from random import randint, random


def my_function(name='No name', lastname='No lastname'):
    print(f'Hello {name}\n')	

my_function(lastname = 'Doe',name='John')
my_function('Doe', 'Jane')


print(random())
number = random.randint(0,9999)
