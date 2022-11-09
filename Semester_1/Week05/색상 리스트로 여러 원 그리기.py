import turtle
t = turtle.Turtle()
t.shape("turtle")

clist = ["yellow", "red", "blue", "green"] # 색상 리스트
for i in range(4):
    t.penup() # 펜을 올린다는뜻 : 펜이 안그려진다. -> 테두리기 필요 없을 때 사용
    t.forward(50)
    t.fillcolor(clist[i]) # 채우기 색상 지정
    t.pencolor(clist[i]) # 펜 색상 지정
    t.begin_fill() # 채우기 시작 -> end와 꼭 같이 사용, 채우기 색을 정한 다음 begin
    t.pendown() # 펜을 내린다는 뜻 : 펜이 다시 그려진다.
    t.circle(100)
    t.end_fill() # 채우기 끝


