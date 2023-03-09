# demo datatypes
b = False
print(b, type(b))

# integer
i = -123
print(i, type(i))

# floating point
f = 1.12
print(f, type(f))

f = float('545')
print(f, type(f))

#  complex numbers
c = 1 + 23j
print(c, type(c))

list1 = [123,4543, '35345', 'Jannes']
print(list1, type(list1))

# get fist index
print(list1[0])

# get last value of list
print(list1[-1])

print(list1[3:])

list1[0] = 'Jannes'
print(list1[0])

t = (123,342.54, 'test')
# tuples kan je niet aanpassen, voor de rest hetzelfde als list 
#  t[0] = 'test'

#  ranges
r = range(5)

print(list(r))

r = range(4, 675, 23)
print(list(r))

#  text
name = "Jannes"

fullText = '''fdsf
fdsfsdf
'''
print(fullText.capitalize())

#  set
s = {
    1, 2.0, 'drie'
}

print(s, type(s))

for item in s: 
    print(item, type(item))

# dictionaries
d = {'one': 1, '2': 3}
for key in d:
    print(key, d[key], type(key), type(d[key]))

d = dict([('one', 1),('one', 1)])
for key in d:
    print(key, d[key], type(key), type(d[key]))

text = input('Welke input?')

# oefening 1
# maak een persoon aan in een dictionary met naam, leeftijd 
# en stad en druk de gegevens af
name = input('Naam: ')
age = int(input('Leeftijd: '))
city = input('Stad: ')

person = {
    'name': name,
    'age': age,
    'city': city
}

for key in person:
    print(key, person[key])

