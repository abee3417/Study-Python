import turtle
import random

t1 = turtle.Turtle()
t1.penup()

a = int(turtle.textinput("동전 던지기 게임","0(그림) 또는 1(숫자)을 입력하시오"))
# 사용자가 0, 1중 선택
coin = random.randint(0,1)
# 사용방법 : 변수 = random.randint(초기값, 끝값)
# 초기값 ~ 끝값 (이 두값은 포함) 의 정수 중 하나를 변수에 할당

screen = turtle.Screen()
# 변수 = turtle.Screen() : 터틀 라이브러리의 스크린을 불러온다.
image1 = "front.GIF"
image2 = "back.GIF"
screen.addshape(image1)
screen.addshape(image2)
# 변수.addshape(파일이름) : 변수에 이미지를 추가한다.

if coin == 0 : # coin이 0일땐 image1을 사용
    t1.shape(image1)
    t1.stamp()
    # 변수.stamp() : 스크린에 모양을 도장처럼 찍어준다. (이미지가 스크린에 뜨도록)
else : # coin이 1일땐 image2을 사용
    t1.shape(image2)
    t1.stamp()
    
t2 = turtle.Turtle()
t2.penup()
if coin == a : # 사용자의 선택과 프로그램의 선택이 같아야 승리
    t2.goto(0,100)
    t2.write("승리",font=("Arial",20,"normal"))
    # font = ("글씨체", 글씨크기, "글씨특징(진하게, 밑줄 등)")
else :
    t2.goto(0,100)
    t2.write("패배",font=("Arial",20,"normal"))
