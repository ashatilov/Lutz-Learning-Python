def is_prime(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x = x - 1
    else:
        print(y, 'is prime')

is_prime(4)
is_prime(13.0)
is_prime(-4)
