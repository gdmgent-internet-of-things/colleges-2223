from unittest import mock


x = 16
y = 56

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x > y:
    print('x > y: x is {} and y is {}'.format(x, y))
else:
    print(f'{x} is equal to {y}')

print('x < y: x is {} and y is {}'.format(x, y)) if x < y else print('Check some other stuff!')

# No switch / case you have to do it with if / elif / else
switcher = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}
print(switcher.get(13, 'Invalid month!'))