words = [
    'HTML',
    'CSS',
    'JavaScript',
    'TypeScript',
    'React',
    'Sass',
    'Nest.js',
    'TypeORM'
]
i = 0
while (i < len(words)):
    print(f'word with index {i} and value {words[i]}')
    i += 1

for v in words:
    print(v)

for index, val in enumerate(words):
    print(f'word with index {index} and value {val}')

# Fibonacci
a, b = 0, 1
while b < 1000:
    print(b, end=' ', flush=True)
    a, b = b, a + b
print()

# The secret word
secret = 'swordfish'
pswd = None

while pswd != secret:
    pswd = input('What is the secret word? ')
print('The secret is OK')