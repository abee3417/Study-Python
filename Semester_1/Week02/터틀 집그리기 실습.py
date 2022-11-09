import turtle
t = turtle.Turtle("turtle")
size = int(input("집의 크기는 얼마로 할까요? : "))
i = 0
while(i < 4):
    t.fd(size)
    t.rt(90)
    i += 1
t.lt(60)
t.fd(size)
t.rt(120)
t.fd(size)
t.rt(120)
t.fd(size)

