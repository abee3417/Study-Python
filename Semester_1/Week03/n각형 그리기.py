import turtle
t = turtle.Turtle()
t.shape("turtle")
angle = int(input("몇각형을 그리시겠어요? : "))

for i in range (angle) :
    t.fd(100)
    t.lt(360 // angle)
