A = {1,2,4,3,5,6}
B = {6,4,7,9,8} 
print(A|B)
print(B|A)
print(A&B)
print(B&A)
print(A-B)
print(B-A)
print(A^B)

x = {7,8,9,10}
y = {7,8,9,10,11,12,13,14}
print(x.issubset(y))
print(y.issubset(x))
print(x.isdisjoint(y))
print(y.isdisjoint(x))
print(x.issuperset(y))
print(y.issuperset(x))

x = [10,10,55,22,55,22]
xs = set(x)
xl = list(set(x))
print(x)
print(xs)
print(xl)