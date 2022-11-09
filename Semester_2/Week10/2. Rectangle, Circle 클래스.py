class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        print("계산 불가능")
    def perimeter(self):
        print("계산 가능")

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h
    def area(self): # 오버라이딩
        return self.w * self.h
    def perimeter(self): # 오버라이딩
        return 2 * (self.w + self.h)

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r
    def area(self): # 오버라이딩
        return 3.14 * self.r**2
    def perimeter(self): # 오버라이딩
        return 2 * 3.14 * self.r

r = Rectangle(0, 0, 100, 200)
print("사각형의 면적", r.area())
print("사각형의 둘레", r.perimeter())

c = Circle(0, 0, 100)
print("원의 면적", c.area())
print("원의 둘레", c.perimeter())
