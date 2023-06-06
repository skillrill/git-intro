# create a class
class Rectangle:

    # create a constructor method
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
    

    # create an object method
    def get_area(self):
        area = self.height * self.width
        return area


rect1 = Rectangle(10, 50)
rect2 = Rectangle(44, 100)

print(rect1.get_area())
print(rect2.get_area())