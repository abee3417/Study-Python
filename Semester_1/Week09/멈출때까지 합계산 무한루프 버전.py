# 무한루프 버전
total = 0
while True: # True False 앞글자는 대문자
    num = int(input("숫자를 입력하시오: "))
    total += num
    choice = input("계속?(yes/no) : ")
    
    if (choice == 'no'):
        print("합계는 : %s" %total)
        break;

