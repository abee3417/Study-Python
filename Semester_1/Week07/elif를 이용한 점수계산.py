score = int(input("점수를 입력하세요 : "))
if score >= 90 : # score >= 90
    print("A학점")
elif score >= 80 : # 80 <= score < 90
    print("B학점")
elif score >= 70 : # 70 <= score < 80
    print("C학점")
else : # score < 70
    print("D학점")
