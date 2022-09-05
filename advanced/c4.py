from hashlib import blake2b


class Calculation1:
    def summation(self, a,b):
        return a+b;
class Calculation2:
    def Multiplication(self, a, b):
        return a*b;
class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a/b;
d = Derived()
print(d.summation(10, 20))
print(d.Multiplication(10, 20))
print(d.Divide(10, 20))