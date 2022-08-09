x = [2,5,8,7,3,6,9]
x2 = [i**2 for i in x]
print(x2)
y = [2,3,5,6,7,8,9]
z = [i+j for i,j in zip(x,y)]
print(z)