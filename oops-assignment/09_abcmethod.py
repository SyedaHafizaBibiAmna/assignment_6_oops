from abc import abstractmethod,ABC


class Shape(ABC):

    @abstractmethod
    def area(self): 
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  


react = Rectangle(5, 10)
print(react.area())  # Output: 50      



class Cricle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
        
cir = Cricle(5)
print(cir.area())  # Output: 78.5        

