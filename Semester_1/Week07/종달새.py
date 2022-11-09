import random
time = random.randint(1, 24) # 1부터 24까지 정수 중 랜덤
print("안녕하세요! 지금 시각은 %s시 입니다." %time)

sunny = random.choice([True, False]) # 괄호 리스트 중 랜덤으로 선택

if sunny : # if (sunny == True)와 같다.
    print("현재 날씨가 화창합니다.")
else :
    print("현재 날씨가 화창하지 않습니다.")

# 종달새가 노래를 할 것인지를 판단해보자.

if (6 <= time < 9) and (sunny) : # (time >= 6) and (time < 9)
# 파이썬은 c와 다르게 삼항연산자가 된다.
    print("지지배배지지배배!!!")
else :
    print("종달새가 조용합니다.")

