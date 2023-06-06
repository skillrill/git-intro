class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self, increment):
        self.speed += increment
    
    def brake(self, decrement):
        self.speed -= decrement
        if self.speed < 0:
            self.speed = 0
    
    def display_speed(self):
        print(f"Current speed: {self.speed} mph")

# Creating car objects
car1 = Car("Ford", "Mustang", 2022)
car2 = Car("Tesla", "Model S", 2023)

# Accelerating and braking
car1.accelerate(40)
car1.display_speed()  # Output: Current speed: 40 mph

car2.accelerate(60)
car2.brake(20)
car2.display_speed()  # Output: Current speed: 40 mph