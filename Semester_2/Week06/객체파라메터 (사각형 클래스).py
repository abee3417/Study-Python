#사각형 클래스
class Rect:
    def __init__(self, side = 0):
        self.side = side
    def getArea(self):
        return self.side * self.side

#파라메터로 클래스 객체가 들어갈 수 있다.
def printAreas(r, n):
    for i in range (n):
        print("반지름 = %s, \t넓이 = %s" %(r.side, r.getArea()))
        r.side += 1
    while n >= 1:
        print("반지름 = %s, \t넓이 = %s" %(r.side, r.getArea()))
        r.side = r.side + 1
        n = n - 1

myRect = Rect()
count = 5
printAreas(myRect, count)
print("사각형의 변 =", myRect.side)
print("반복횟수 =", count)
