from abc import ABC
import math

class shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area (self):
        return self.radius * math.pi ** 2
    def calculate_perimeter(self):
        return self.radius * math.pi * 2
class rectangle(shape):
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width
    def calculate_area(self):
        return self.hight * self.width
    def calculate_perimeter(self):
        return ( self.hight + self.width) * 2
circle = circle(5) 
print(circle.calculate_area()) 
print(circle.calculate_perimeter()) 
rectangle = rectangle(10, 20) 
print(rectangle.calculate_area()) 
print(rectangle.calculate_perimeter())


    