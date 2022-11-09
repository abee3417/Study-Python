### 전역변수와 지역변수 ###
def calculate_area(radius):
    
    # area = 3.14 * radius ** 2
    # 이렇게 하면 0이 출력되므로, 'global'붙여 전역변수로 바꿔준다.
    # 사용법 : global + 변수명
    
    global area
    area = 3.14 * radius ** 2 # global을 사용할 땐 한번에 초기화 x
    return

area = 0
r = float(input("원의 반지름 : "))
calculate_area(r)
print(area)

# 기존의 전역변수 area = 0은 함수 실행 전에 선언됬으므로 함수 내 area로 전역변수가 바뀐다.
# 만약 area = 0전에 함수를 실행했다면 area는 0으로 전역변수가 바뀐다.
