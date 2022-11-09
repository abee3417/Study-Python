import turtle

t = turtle.Turtle("turtle")
t.circle(100) # circle 괄호 안에는 반지름
for i in range (5) :
    t.fd(100)
    t.lt(360 / 5) # 오각형 작성

# rt는 right의 줄임말, lt는 left의 줄임말
