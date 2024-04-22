class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0  # Initial speed is set to 0

    # Getter method for brand attribute
    def get_brand(self):
        return self.__brand

    # Setter method for brand attribute
    def set_brand(self, brand):
        self.__brand = brand

    # Getter method for model attribute
    def get_model(self):
        return self.__model

    # Setter method for model attribute
    def set_model(self, model):
        self.__model = model

    # Getter method for year attribute
    def get_year(self):
        return self.__year

    # Setter method for year attribute
    def set_year(self, year):
        self.__year = year

    # Getter method for speed attribute
    def get_speed(self):
        return self.__speed

    # Method to accelerate the car
    def accelerate(self, increment):
        self.__speed += increment

    # Method to decelerate the car
    def decelerate(self, decrement):
        self.__speed -= decrement

# Creating an instance of Car
my_car = Car("Toyota", "Corolla", 2022)

# Accessing and modifying attributes using getter and setter methods
print("Brand:", my_car.get_brand())  # Output: Toyota
print("Model:", my_car.get_model())  # Output: Corolla
print("Year:", my_car.get_year())    # Output: 2022

my_car.set_model("Camry")  # Changing the model using setter method
print("Model:", my_car.get_model())  # Output: Camry

# Accelerating the car
my_car.accelerate(30)
print("Speed:", my_car.get_speed())  # Output: 30

# Decelerating the car
my_car.decelerate(10)
print("Speed:", my_car.get_speed())  # Output: 20
