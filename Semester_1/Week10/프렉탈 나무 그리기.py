## 시험 x 참고용 ##
import turtle
def tree(length):
    if length > 5:
        t.forward(length)
        t.rt(20)
        tree(length - 15) # 재귀 호출
        t.lt(40)
        tree(length - 15)
        t.rt(20)
        t.backward(length) # 길이만큼 뒤로감
t = turtle.Turtle()
t.lt(90)

t.color("green")
t.speed(1)
tree(90) # 길이 90으로 시작
