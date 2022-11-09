import turtle
t = turtle.Turtle()
# turtle 생성의 기본 툴
t.shape("turtle")
# 커서모양 바꾸기는 t.shape("모양")
angle = int(input("몇각형을 그리시겠습니까? : "))
    
# 반복문을 생성
for i in range(angle) :
    t.fd(100)
    t.lt(360 / angle)

# while문으로 바꾼다면
'''
i = 0
while i < angle :
    t.fd(100)
    t.lt(360 / angle)
    i += 1
'''

# 반복문 추가설명
'''
- for문의 기본 툴 -> for 횟수세는변수 in range(반복횟수) :
- range(시작위치, 끝나는위치, 증가하는 수치)
- range(4) = range(0,4) = range(0,4,1)
- 파이썬에서는 ~까지는 그 전까지만 포함한다. (위의 예시에서는 0,1,2,3 이렇게 4번반복)
- c언어에서 for(i = 0; i < 8; i++) -> 파이썬에서 for i in range(0, 8, 1)
- 시작점이 0, 반복문의 수치가 1씩 증가한다면 for i in range(8)도 가능한 것이다.
'''
