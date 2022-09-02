
class Dog:
    age = 0
    weight = 0
    height = 0
    breed = ""
    color = ''
    gender = ''

    def bark(self):
        print('🐶bow'*3)
    
    def wag(self):
        print('wags tails')
    
    def eat(self, food):
        print(f'dog {food} is eating')



Bruno = Dog() #calling the consttructor 
Bruno.age = 4
Bruno.breed = 'street dog'
Bruno.color = 'black'
Bruno.weight = 5
Bruno.height = 1
Bruno.gender = 'male'


charlie = Dog()
charlie.age = 3
charlie.breed = 'Husky'
charlie.color = 'white'
charlie.weight = 3
charlie.height = 8
charlie.gender = 'female'

Jimmy = Dog()
Jimmy.age = 5
Jimmy.breed = 'Bull dog'
Jimmy.color = 'brown'
Jimmy.weight = 7
Jimmy.height = 5
Jimmy.gender = 'male'

Bruno.bark()
Bruno.eat('fish')
charlie.eat('dog food')
Jimmy.bark()
charlie.eat('roti')