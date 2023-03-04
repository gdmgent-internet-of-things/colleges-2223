def messages_with_dirrent_print():
    print('The value is %d' % 42)
    print('The values are %d %d' % (54, -13))

    x = 37
    print(f'The value of x is {x}')

def main():
    print('Application started')
    if False:
        print('It\'s True')
    else:
        print("It's not true -> False")

    messages_with_dirrent_print()

if __name__ == '__main__': main()