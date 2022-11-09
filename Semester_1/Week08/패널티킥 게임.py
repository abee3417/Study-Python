import random

options = ["왼쪽", "중앙", "오른쪽"]
c_choice = random.choice(options) # options의 리스트중 랜덤으로 선택
# c_choice = random.choice(["왼쪽", "중앙", "오른쪽"])
u_choice = input("어디를 공격하시겠어요? (왼쪽, 중앙, 오른쪽) ")

if (u_choice == c_choice) : # 방향이 같으면 실패
    print("사용자는 %s을 공격하였고, 컴퓨터는 %s를 막아 패널티킥이 실패했습니다." %(u_choice, c_choice))
else : # 다르면 성공
    print("사용자는 %s을 공격하였고, 컴퓨터는 %s를 막아 패널티킥이 성공했습니다." %(u_choice, c_choice))
