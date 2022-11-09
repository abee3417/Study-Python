import turtle
import random


data = [120, 56, 309, 220, 156, 23, 98]
clist = ["red", "green", "blue", "yellow"]

t = turtle.Turtle()
t.color("blue") # 펜색 : 파랑
t.pensize(3)

def drawBar(height):
    t.fillcolor(random.choice(clist))
    t.begin_fill()
    t.lt(90)
    t.fd(height)
    t.write(str(height), font = ('Times New Roman', 16, 'bold'))
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()
    
for i in range(7): # for i in data:
    drawBar(data[i]) # drawBar(i)
    
t.hideturtle() # 거북이의 커서를 없앰
