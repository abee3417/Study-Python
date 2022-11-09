import turtle
t = turtle.Turtle()
t.shape("turtle")

# a = input("이름을 입력하시오 : ")

a = turtle.textinput("인사", "이름을 입력하시오 : ")
# textinput의 형식 : turtle.textinput("제목 표시줄의 이름", "설명줄")
# textinput은 다른 변수를 만들어준다. (t.textinput은 X)

t.write("안녕하세요? %s씨, 터틀 인사드립니다.\n" %a)
# write는 터틀 창에 작성하는 내용으로, 반드시 한문장으로 끝내야한다.
# c언어와 같이 \n으로 엔터 입력이 가능하다.
t.write(a * 3)
# textinput도 문자열로 저장되므로 출력이 가능하다.

t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
