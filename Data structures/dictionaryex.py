my_dict = {'name': 'Nikita', 'age': 20}
print(my_dict['name'])
print(my_dict.get('age'))


#create a dictionary
squares = {2: 4, 3: 9, 4: 16, 8: 64}
print(squares.pop(3))

for i in squares:
    print(i)
for i in squares:
    print(squares[i])
for k,v in squares.items():
    print(k,v)