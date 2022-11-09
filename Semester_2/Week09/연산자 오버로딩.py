### 연산자 오버로딩 ###
# 파이썬에서 기본적인 오버로딩은 존재x, 연산자 오버로딩만 존재
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __add__(self, other):
        # 객체(클래스)가 파라메터로 들어간다. 여기선 self : p1, other : p2
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y) # 새로운 객체를 리턴
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
    
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2 # 원래는 안되지만, 가능하게 해주기 위해 add를 재정의
print(p3) # 결과 : (4, 6)

