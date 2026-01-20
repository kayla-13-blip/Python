from abc import ABC
class Polygon(ABC):
    def __init__(self, name):
        self.__name = name  
    def get_name(self):
        return self.__name
    def calculate_area(self):
        pass
class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._name = "Square" 
    def get_name(self):
        return "Square"
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base * self.height
def display_area(shape):
    print(f"The area of the {shape.get_name()} is: {shape.calculate_area()}")
shapes = [
    Rectangle(10, 5),
    Square(4),
    Triangle(6, 8)
]
for s in shapes:
    display_area(s)
