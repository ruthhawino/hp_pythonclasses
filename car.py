class Car:
    num_wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("The car is starting.")
       

    def stop(self):
        print("The car is stopping.")

    def drive(self):
        print("The car is being driven.")
        

car1 = Car("Nissan", "pathfinder", 1985)
car1.start()
car2 = Car("Honda", "Civic", 2023)
car2.drive()
