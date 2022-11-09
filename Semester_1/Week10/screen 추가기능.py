screen.onkey(turn_left, "Left") # Left를 눌렀을 때 turn_left를 실행. -> 대소문자 주의!
screen.onkey(turn_right, "Right") # Right를 눌렀을 때 turn_right를 실행 -> 대소문자 주의!

screen.listen() # 키보드의 입력을 받을때까지 (listen) 대기
screen.mainloop() # mainloop()선언한 바로 윗줄까지를 계속 반복 (그러므로 가장 밑에 써줘야 한다.)
