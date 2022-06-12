a = [1,2,3,4,9,9,9]
b = [6,7,8,9,10]

c = list(map(lambda i,j: i + j, a, b))
print(c)