# 오리지널 버전
total = 0
choice = 'yes' # 무한루프가 아니므로 choice를 선언하고 초기화
while choice == 'yes' :
    num = int(input("숫자를 입력하시오: "))
    total += num
    choice = input("계속?(yes/no) : ")

print("합계는 : %s" %total)
