class Animal:
    def eat(self):
        print("The animal is eating")

class Bird(Animal):
    def fly(self):
        print("The animal is flying")

class Mammal(Animal):
    def breastfeed(self):
        print("The animal is nursing")

class Bat(Mammal, Bird):
    pass

bird = Bird()
bird.eat()

print(Bat.mro())
