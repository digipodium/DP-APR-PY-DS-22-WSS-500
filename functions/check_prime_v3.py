
def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "not prime"
    else:
        return "prime"


for i in range(2, 100):
    out = check_prime(i)
    print(i, out)
