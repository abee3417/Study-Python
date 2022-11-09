# 무한루프 버전
import random
num = random.randint(1, 100)
print("1부터 100 사이의 숫자를 맞추시오")
count = 1
while True:
    user = int(input("숫자를 입력하시오 : "))
    if (user == num): # break로 무한루프 탈출
       print("축하합니다. 정답은 %s, 시도횟수 %s번" %(num, count))
       break;
    elif (user < num):
        print("높음!")
    elif (user > num):
        print("낮음!")
    count += 1
