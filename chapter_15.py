class Rectangle:
    all_rectangles = []
    def __init__(self, h=1, w=1):
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

