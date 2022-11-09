import math

def calCircle(r):
    area = math.pi * r * r
    circum = 2* math.pi * r
    return (area, circum) # 리턴을 튜플로 함

radius = float(input("원의 반지름을 입력하시오: "))

# (a, c) = calCircle(radius)
t = calCircle(radius) # 이때 t의 타입은 튜플이다.

# print("원의 넓이는 {}이고 원의 둘레는 {}이다.".format(str(a), str(s)))
print("원의 넓이는 {}이고 원의 둘레는 {}이다.".format(str(t[0]), str(t[1])))
print("원의 넓이는 %s이고 원의 둘레는 %s이다." %(str(t[0]), str(t[1])))
print("원의 넓이는 " + str(t[0]) + "이고 원의 둘레는 " + str(t[1]) + "이다.")
