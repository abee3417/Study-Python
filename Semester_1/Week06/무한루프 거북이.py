import turtle

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.shapesize(3,3) # 거북이를 (세로, 가로) 3배 확대

while True: # while True 사용 -> 무한루프
    command = input("input : ")
    if command == 'l':
        t.left(90)
    if command == 'r':
        t.right(90)
    if command == 'f':
        t.forward(100)
    if command == 'x':
        break

