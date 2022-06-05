import random

def say_hello():
    msg = ['Hello','Namaste','Hola','Bonjour','Guten Tag']
    return random.choice(msg)


out = say_hello()
print(out)

