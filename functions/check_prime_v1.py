def check_prime():
    a = 230913
    for i in range(2, a):
        if a % i == 0:
            print(a, 'is not a prime number')
            break
    else:
        print(a, 'is a prime number')

check_prime()
