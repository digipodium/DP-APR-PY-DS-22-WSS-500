def check_prime():
    a = 13
    for i in range(2, a):
        if a % i == 0:
            return "not prime"
    else:
        return "prime"

out = check_prime()
print(out)
