def main():
    print('Application started!')
    str = 'Hello, World in straße'
    print(str.upper())
    print(str.lower())
    print(str.title())
    print(str.swapcase())
    print(str.casefold()) # spelling in case

    s1 = 'Greetings'
    s2 = 'Earthlings'
    s3 = s1 + ' ' + s2
    print(s3)
    s3 = '{} {}'.format(s1, s2) # string interpolation
    print(s3)
    s3 = '{y} {x}'.format(x=s1, y=s2) # string interpolation
    print(s3)
    s3 = '{1} {0}'.format(s1, s2) # string interpolation
    print(s3)
    s3 = '{1:>016} {0:<016}'.format(s1, s2) # string interpolation
    print(s3)
    x = 42
    print('The number is {:x}'.format(x))
    print('The number is {:o}'.format(x))
    print('The number is {:b}'.format(x))
    print('The number is {:.3f}'.format(x))

    s4 = 'This,is,the,new,society'
    print(s4.replace(',', ' '))

    s5 = 'Like Graphics, Love Code and make Cool Stuff'
    print(s5)
    s6 = s5.split()
    print(s6)
    s7 = ':'.join(s6)
    print(s7)

if __name__ == '__main__': main()