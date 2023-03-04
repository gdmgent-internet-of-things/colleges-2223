secret = 'swordfish'
passwd = None
count = 0
max_attempt = 5
auth = False

while passwd != secret:
    count += 1
    if count > max_attempt: 
        break
    passwd = input(f'{count}: What\'s the secret word? ')
else:
    auth = True

print('Authorized' if auth else 'Calling the police!')