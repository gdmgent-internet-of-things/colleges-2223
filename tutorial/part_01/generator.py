def main():
    for i in inclusive_range(25):
        print(i, end = ' ', flush=True)
    print()

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

if __name__ == '__main__': main()