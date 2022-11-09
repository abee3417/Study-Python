import random
import turtle

def draw_maze(x, y):
    for i in range(2): # 미로를 만드는 for문
        t.penup()
        if i == 1:
            t.goto(x + 100, y + 100)
        else:
            t.goto(x, y)
        t.pendown()
        t.fd(300)
        t.rt(90)
        t.fd(300)
        t.lt(90)
        t.fd(300)
def turn_left():
    t.lt(10)
    t.fd(10)
def turn_right():
    t.rt(10)
    t.fd(10)

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0)

draw_maze(-300, 200)
screen.onkey(turn_left, "Left")
# Left를 눌렀을 때 turn_left 함수를 실행. -> 대소문자 주의!
screen.onkey(turn_right, "Right")
# Right를 눌렀을 때 turn_right를 실행 -> 대소문자 주의!

t.penup()
t.goto(-300, 250)
t.speed(1)
t.pendown()
screen.listen() # 키보드의 입력을 받을때까지 (listen) 대기
screen.mainloop() # mainloop()선언한 바로 윗줄까지를 계속 반복 (그러므로 가장 밑에 써줘야 한다.)
