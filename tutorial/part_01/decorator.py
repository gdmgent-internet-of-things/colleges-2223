def main():
    x = f3()
    print(x)

def f1(f):
    def f2():
        print('this is before f')
        f()
        print('this is after f')
    return f2

@f1
def f3():
    print('this is f3')

if __name__ == '__main__': main()