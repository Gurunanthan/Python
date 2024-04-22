class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__private_attribute = "secret"
        self._protected_attribute = "protected"

    def public_method(self):
        print("This is a public method")

    def __private_method(self):
        print("This is a private method")

    def _protected_method(self):
        print("This is a protected method")

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday! Now I am {self.age} years old.")

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        self.__private_attribute = value

# Creating an instance of MyClass
obj = MyClass("Alice", 30)

# Accessing and manipulating attributes and calling methods
print(obj.name)               # Output: Alice
print(obj.age)                # Output: 30
print(obj.get_private_attribute())  # Output: secret

obj.public_method()          # Output: This is a public method
obj.greet()                  # Output: Hello, my name is Alice and I am 30 years old.
obj.birthday()               # Output: Happy birthday! Now I am 31 years old.
print(obj.age)               # Output: 31

obj.set_private_attribute("new secret")
print(obj.get_private_attribute())  # Output: new secret
