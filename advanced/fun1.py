#syntax
#def fun_name([parameter])
#   statements
#   [return expressions]

#defining
def hello():
    print('hello')
    print('world')

#calling or using
hello()
hello()

def greetings(message):
    print('🐼',message)
greetings('world')
greetings('hola')
greetings('namaste doston')


def calc_area(w, h):
    area = w*h
    print('area:', area)
calc_area(5, 6)
calc_area(10, 20)
calc_area(100,500)


def calc_area_v2(w, h):
    area = w*h
    return area

#display
print(calc_area_v2(5, 8))
print(calc_area_v2(7, 8))

#storing return value in a variable
ans = calc_area_v2(5, 8)
print(ans)

#using return value in expression
ans = calc_area_v2(7,8) + calc_area_v2(5, 8)
print(ans)