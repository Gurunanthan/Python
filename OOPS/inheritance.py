class Car:
    def __init__(self, brand, model, year, color, ownerName):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.ownerName = ownerName
        self.statusOfCar = False  

    def createCar():
        brand = input("Enter brand of the car: ")
        model = input("Enter model of the car: ")
        year = input("Enter year of the car: ")
        color = input("Enter color of the car: ")
        ownerName = input("Enter owner's name: ")
        return Car(brand, model, year, color, ownerName)
    
    def owner(self):
        print(self.ownerName + " is the owner of the car")

    def status(self):
        if self.statusOfCar:
            print("The car is running")
        else:
            print("The car has been stopped")

    def start(self):
        if self.statusOfCar:
            print("The car is already running")
        else:
            print("Starting the car...")
            self.statusOfCar = True

    def stop(self):
        if not self.statusOfCar:
            print("The car has already been stopped")
        else:
            print("Stopping the car...")
            self.statusOfCar = False

    def displayDetails(self):
        print("Model:", self.model)
        print("Brand:", self.brand)
        print("Year:", self.year)
        print("Color:", self.color)
        print("Owner:", self.ownerName)


class nissan(Car):

    def madeCompany():
        print("Made in Japan")


gtr = nissan.createCar()
gtr.displayDetails()
gtr.status()
gtr.start()
gtr.status()
gtr.stop()
nissan.madeCompany()  
