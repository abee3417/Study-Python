import turtle
t = turtle.Turtle()
t.shape("turtle")

shape = turtle.textinput("", "도형을 입력하시오 :")
if (shape == "삼각형"):
    length = int(turtle.textinput("", "한번의 길이 :"))
    for i in range (3):
        t.fd(length)
        t.lt(120)   

elif (shape == "사각형"):
    width = int(turtle.textinput("", "가로 :"))
    height = int(turtle.textinput("", "세로 :"))
    for i in range (2):
        t.fd(width)
        t.lt(90)
        t.fd(height)
        t.lt(90)

elif (shape == "원"):
    radius = int(turtle.textinput("", "반지름의 길이 :"))
    t.circle(radius)
    
