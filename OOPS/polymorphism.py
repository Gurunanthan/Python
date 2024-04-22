class Poly:
    def calculate(self, a, b, c=None):
        if c is not None:
            print("It is printed from the second function which takes three arguments")
            print(a + b + c)
        else:
            print("It is printed from the first function which takes two arguments")
            print(a + b)

p = Poly()

p.calculate(1, 2)

p.calculate(1, 2, 3)



class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof woof")

class Cat(Animal):
    def make_sound(self):
        super().make_sound() # to call the above class method
        print("Meow")

animal = Animal()
dog = Dog()
cat = Cat()

print("Animal:")
animal.make_sound()

print("Dog:")
dog.make_sound()

print("Cat:")
cat.make_sound()
