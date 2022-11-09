import turtle
t = turtle.Turtle()

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def drawit(x, y): # x, y는 클릭 좌표
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color("green")
    square(50)
    t.end_fill()

s = turtle.Screen() # 그림이 그려지는 캔버스 생성
s.onscreenclick(drawit)
# screen함수 안에 있는 기능인 onscreenclick
# 이벤트가 실행되면 drawit함수를 실행 (콜백 함수)
# 변수.onscreenclick(함수) : 클릭한 좌표를 함수로 보냄
drawit(0, 0) # 0, 0에서 하나 만들고 시작

s.listen()
s.mainloop()
