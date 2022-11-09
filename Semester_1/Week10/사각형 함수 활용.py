import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range (4):
        t.fd(length)
        t.lt(90)


t.penup()
t.goto(-200, 0)
t.pendown()
square(100)

t.penup()
t.goto(0, 0)
t.pendown()
square(100)

t.penup()
t.goto(200, 0)
t.pendown()
square(100)
