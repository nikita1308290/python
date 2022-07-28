val = int(input('>>Enter a Number:'))
if val > 100 :
    val = val/2
else :
    val = val*2
print('>>the result is:', val)

# true situation if condition else false situation

val = int(input('>>Enter a number'))
val = val/2 if val > 100 else val *2
print('>>The result is:', val)

name = input("Enter your name:")
if name.isalpha() :
    print("very good")
else :
    print("Not good")

name = input("Enter your name")
print('very good') if name.isalpha() else print('Not good')