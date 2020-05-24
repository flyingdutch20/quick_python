class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y

class Circle(Shape):
    all_circles = []
    pi = 3.14159
    def __init__(self, r=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = r
        self.__class__.all_circles.append(self)
    @classmethod
    def total_area(cls):
        area = 0
        for circle in cls.all_circles:
            area += cls.circle_area(circle.radius)
        return area
    @staticmethod
    def circle_area(radius):
        return Circle.pi * radius * radius

class Rectangle(Shape):
    all_rectangles = []
    def __init__(self, h=1, w=1):
        super().__init__(x, y)
        self.height = h
        self.width = w
        self.__class__.all_rectangles.append(self)
    def area(self):
        return self.height * self.width
    def circumfence(self):
        return 2 * (self.height + self.width)

    @classmethod
    def total_area(cls):
        total = 0
        for rect in cls.all_rectangles:
            total = total + rect.area()
        return total

    @classmethod
    def total_circumfence(cls):
        total = 0
        for rect in cls.all_rectangles:
            total = total + rect.circumfence()
        return total

