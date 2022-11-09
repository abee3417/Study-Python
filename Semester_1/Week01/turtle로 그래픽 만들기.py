import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()

turtle.bgcolor("black") # 배경화면은 t.이 아닌 turtle.bgcolor
t.speed(0) # 0은 가장 빠른 스피드로 설정해준다.
t.width(3) # 그리는 펜의 두께를 설정

'''
# while문 사용
length = 10
while length < 500:
    t.forward(length)
    t.pencolor(colors[length % 6])
    # 길이를 6으로 나눈 나머지가 계속 변하면서 색깔을 변경
    t.right(89) # 89도로 꺾어지면서 진행
    length += 5 # length = length + 5
'''

# for문 사용
for length in range (10, 500, 5) :
    t.forward(length)
    t.pencolor(colors[length % 6])
    # 길이를 6으로 나눈 나머지가 계속 변하면서 색깔을 변경
    t.right(89) # 89도로 꺾어지면서 진행
