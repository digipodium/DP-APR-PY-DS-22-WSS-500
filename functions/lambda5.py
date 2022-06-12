x= list(range(1,1001))

x35 = list(filter(lambda i: i % 3 ==0 and i % 5==0, x))
print(x35)