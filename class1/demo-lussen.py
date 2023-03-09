iteration = 0
stop = 5
is_true = True
while is_true:
    print(f'iteration {iteration}')   
    iteration += 1
    if iteration >= stop:
        is_true = False

print(f'iteration {iteration}')  

for character in 'Lorem':
    print(character)

for number in range(1, 5 + 1, 2):
    print(number)

# enumarate
start = 0
stop = 100
step = 20
r = range(start, stop +1, step)

for count, value in enumerate(r):
    print(f'count: {count}, value: {str(value).rjust(3)}')
    continue
    print('dit wordt niet uitgevoerd')

while True:
    answer = input('Answer: ')
    if 0 < len(answer):
        print(f'Your answer: {answer}')
        break
print('end')

# Oefening 3
# Vraag aan iemand hoelang te tellen
# Bij elke tel vraag je of de persoon wil stoppen
# Toon gepaste boodschap na het tellen
stop = int(input('Hoe lang wil je tellen? '))
for i in range(1, stop + 1):
    print(i)
    stillCounting = input('Wil je verder tellen? (y/n) ')
    if stillCounting == 'n':
        break
print('Gedaan met tellen')