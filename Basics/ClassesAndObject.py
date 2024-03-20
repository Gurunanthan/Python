import os
class example:
    def __init__(self,age,name):
        self.name = name
        self.age = age
    def person(self):
        print("name: %s" % self.name)
        print("age: %s" % self.age)


x = example(5,"person")
x.person()

