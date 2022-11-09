math = int(input("수학 점수를 입력하세요 : "))
eng = int(input("영어 점수를 입력하세요 : "))
total = math + eng
if total < 110 :
    print("총합 점수 부족으로 불합격입니다.")
elif eng < 40 :
    print("영어 점수 부족으로 불합격입니다.")
elif math < 40 :
    print("수학 점수 부족으로 불합격입니다.")
else :
    print("합격입니다. 축하드립니다.")
# 순서도(알고리즘) 그리는것도 잘 볼것.
