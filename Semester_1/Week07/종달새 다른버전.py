import random
for i in range (5):
    time = random.randint(1, 24) # 1부터 24까지 정수 중 랜덤
    print("안녕하세요! 지금 시각은 %s시 입니다." %time)

    weather = random.choice(['sunny', 'cloudy', 'rainy'])
    # 괄호 리스트 중 랜덤으로 선택
    # 리스트에 문자열 쓸거면 문자열 기호 꼭 넣기

    if (weather == 'sunny'):
        print("현재 날씨가 화창합니다.")
    elif (weather == 'rainy'):
        print("현재 비가 오고 있습니다.")
    else :
        print("현재 날씨가 흐립니다.")

    # 종달새가 노래를 할 것인지를 판단해보자.

    if (6 <= time <= 12) and (weather == 'sunny') :
    # (time >= 6) and (time >= 12)
    # 파이썬은 c와 다르게 삼항연산자가 된다.
        print("지지배배지지배배!!!")
    else :
        print("종달새가 조용합니다.")
    print("\n")

