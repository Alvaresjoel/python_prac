class Rectangle :
    def __init__(self,breath,width):
        self.breath = breath
        self.width = width

    def calculate_area(self):
        area = self.breath * self.width
        return area

Rectangleobject = Rectangle(10,10)
Rectangleobject2 = Rectangle(10,20)
print(Rectangleobject.calculate_area())
print(Rectangleobject2.calculate_area())