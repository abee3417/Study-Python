# 오리지널 버전
import random
num = random.randint(1, 100)
print("1부터 100 사이의 숫자를 맞추시오")
count = 0
user = 0 # 무한루프가 아니므로 while문 전에 user 선언

while user != num:
    user = int(input("숫자를 입력하시오 : "))
    if (user < num):
        print("높음!")
    elif (user > num):
        print("낮음!")
    count += 1
    
print("축하합니다. 정답은 %s, 시도횟수 %s번" %(num, count))
