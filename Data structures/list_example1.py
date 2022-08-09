x = [7, 5, 3, 12]
x2 = []
for i in x:
    s = i**2
    x2.append(s)

print(x)
print(x2)


x = [2, 3, 5, 4]
y = [3, 6, 5, 3]
z = []

for i,j in zip(x,y): #special loop function
    z.append(i+j)
print(z)