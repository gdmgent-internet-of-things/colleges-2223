def show(n):
    print(n)

show(32)

def show_to(n = 4):
    print(n)

show_to()

def show_withreturn(n = 32):
    return n

x = show_withreturn(64)
print(x)

def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

x = 6
print(f'{x} is prime') if is_prime(x) else print(f'{x} is not a prime')

def list_primes():
    for n in range(100):
        if is_prime(n):
            print(n, end = ' ', flush=True)
    print()

list_primes()
