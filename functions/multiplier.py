def multiplier(*values):
    total = 1
    for value in values:
        total *= value
    return total

def subtraction(*values):
    if values:
        total = values[0]
        for value in values[1:]:
            total -= value
        return total

print(multiplier())
print(multiplier(23, 2, 5))
print(multiplier(1,2,3,4,5))
print(multiplier(23,2,5,1,2,3,4,5,6,7,8,9))

print(subtraction())
print(subtraction(23, 2, 5))
print(subtraction(1,2,3,4,5))
