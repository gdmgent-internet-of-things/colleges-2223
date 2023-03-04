# Define an Animal
class Animal:
    # def __init__(self, type, name, sound) -> None:
    #     self._type = type
    #     self._name = name
    #     self._sound = sound

    def __init__(self, **kwargs) -> None:
        self._type = kwargs['type'] if 'type' in kwargs else 'animal'
        self._name = kwargs['name'] if 'name' in kwargs else 'nameless'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'nosound'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._nqme = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self) -> str:
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

class Duck(Animal):
    def __init__(self, **kwargs) -> None:
        kwargs['type'] = 'duck'
        super().__init__(**kwargs)

class Kitten(Animal):
    def __init__(self, **kwargs) -> None:
        kwargs['type'] = 'kitten'
        super().__init__(**kwargs)

    def kill(self, s):
        print(f'{self.name()} will now kill all {s}!')

class RevStr(str):
    def __str__(self) -> str:
        return super().__str__()[::-1]

def print_animal(animal):
    if not isinstance(animal, Animal):
        raise TypeError(f'print_animal(): requires an Animal object')

    print(f'The {animal.type()} is named "{animal.name()}" and says "{animal.sound()}".')

def main():
    print('Application started!')
    # Create animals
    # animal_1 = Animal('kitten', 'fluffy', 'rwar')
    animal_1 = Animal(type='kitten', name='fluffy', sound='rwar')
    animal_1.sound('meoow')
    print(animal_1)
    # print_animal(animal_1)
    # animal_2 = Animal('duck', 'donald', 'quack')
    animal_2 = Animal(type='duck', name='donald', sound='quack')
    print(animal_2)
    # print_animal(animal_2)
    animal_3 = Duck(name='donald', sound='quack')
    print(animal_3)
    animal_4 = Kitten(name='fluffy', sound='rwar')
    print(animal_4)
    animal_4.kill('humans')

    hello = RevStr('Hello, World')
    print(hello)

if __name__ == '__main__': main()