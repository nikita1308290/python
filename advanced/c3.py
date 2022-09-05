class Fruit:
    color = 'red'
    taste = 'sweet'


class veg:
    size = 'small'
    age = 'fresh'


class GM(Fruit, Veg):
    name = 'GM-122'

g = GN()

print(g.name)
print(g.color)
print(g.taste)
print(g.size)
print(g.age)


