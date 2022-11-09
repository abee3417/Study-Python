import turtle # turtle 모듈을 호출

t = turtle.Turtle() # 변수 t에 모듈을 사용
t.shape("turtle") # t의 모양을 거북이 모양으로 변경
t.fd(200) # fd는 foward의 줄임말로, 앞으로 전진한다는 뜻이다.
t.lt(120) # left로 120도 꺾어진 후,
t.fd(200) # 다시 앞으로 이동 (fd)
t.lt(120) # left로 120도 꺾어진 후,
t.fd(200) # 다시 앞으로 이동 (fd)
t.lt(120) # left로 120도 꺾어진다.

# 파일명과 호출할 모듈명과 이름이 같으면 실행이 안된다. (파일명 turtle은 x)
