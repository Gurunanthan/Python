class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
person = Person(name="guru", age=25, address="dubai main road.dubai")
person.display_details()
