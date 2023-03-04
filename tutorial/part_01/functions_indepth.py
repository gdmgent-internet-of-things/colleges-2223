def main():
    x = kitten()
    print(x)
    x = kitten_things(1, 2)
    print(x)
    x = kitten_arglist('purr', 'grrr', 'meoow')
    x = ('purr', 'grrr', 'meoow')
    x = kitten_arglist(*x)
    x = kitten_keyword_arglist(Buffy = 'meoow', Zilla = 'grrr', Angel = 'rawr')
    x = dict(Buffy = 'meoow', Zilla = 'grrr', Angel = 'rawr')
    x = kitten_keyword_arglist(**x)

def kitten():
    return 'Meoow'

def kitten_things(a, b, c = 3):
    return f'a is {a}, b is {b} and c is {c}'

def kitten_arglist(*args): # variable argument list, is a tuple
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meoow')

def kitten_keyword_arglist(**kwargs): # keyword argument list, is a dictionary
    if len(kwargs):
        for k in kwargs:
            print(f'Kitten {k} says {kwargs[k]}')
    else:
        print('Meoow')

if __name__ == '__main__': main()