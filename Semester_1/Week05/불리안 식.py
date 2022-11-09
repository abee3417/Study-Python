# 그리고 : and, 또는 :  or, 부정 : not
age = 20
height = 160
a = (age >= 10 and height > 165)
# 이런식으로 bool형식으로 나타내라고 하면 반드시 논리식만 써줘야한다. -> 불리언 식
print(a) # False -> height나 165보다 크지 않기 때문

x = True
y = False
print(x and y) # False
print(y or x) # True
c = True
print(x and c) # True
d = False
print(y or d) # False

print("=========================================")

a = 1
b = 10
c = 100
print(a > b and b < c)
# False & True이므로 False가 출력된다.
print(a < b or b > c) # True
print(a > b or b < c) # True
print(a > b or b > c) # False
# or은 앞에 보고 참이면 무조건 True가 출력된다. (모든 조건이 False일때만 False)
