import sys

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # Get paramters from args
    if numargs < 1:
        raise TypeError(f'Expected at least 1 argument, got {numargs} ')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'Expected at most 3 argument, got {numargs} ')

    # Generator
    i = start
    while i <= stop:
        yield i
        i += step

def main():
    print('Application started!')
    try:
        x = 5/0
    except ValueError:
        print(f'I caught a value error!')
    except:
        print(f'Unknow Error: {sys.exc_info()[1]}')
    else:
        print(f'Good job {x}!')

    try:
        for i in inclusive_range():
            print(i, end = ' ', flush=True)
        print()
    except TypeError as e:
        print(f'Range error: {e}')

if __name__ == '__main__': main()