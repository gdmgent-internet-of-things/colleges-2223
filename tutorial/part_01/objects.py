class Student:
    my_quote = 'Like Graphics, Love Code and make cool stuff'

    def study(self):
        print('Studying')

    def do_exercise(self):
        print('Do some exercises')

    def quote(self):
        print(self.my_quote)

def main():
    student = Student()
    student.study()
    student.do_exercise()
    student.quote()

if __name__ == '__main__': main()