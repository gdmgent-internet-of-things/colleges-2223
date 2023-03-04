import os

def main():
    print('Application started!')
    dirname, filename = os.path.split(os.path.abspath(__file__))
    file = dirname + '/data/file.txt'
    f = open(file)
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()