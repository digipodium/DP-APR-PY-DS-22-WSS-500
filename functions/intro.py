# program that finds the hypotenuse

# p = float(input("Enter the length of the First side: "))
# b = float(input("Enter the length of the Second side: "))
# h = (p**2 + b**2)**0.5
# print('Perpendicular: ', p)
# print('Base : ', b)
# print("The hypotenuse is: ", h)

# functions are defined using `def` keyword
# and then we can use these defined function by calling them

def hypotenuse():
    p = float(input("Enter the length of the First side: "))
    b = float(input("Enter the length of the Second side: "))
    h = (p**2 + b**2)**0.5
    print('Perpendicular: ', p)
    print('Base : ', b)
    print("The hypotenuse is: ", h)

# calling
hypotenuse()