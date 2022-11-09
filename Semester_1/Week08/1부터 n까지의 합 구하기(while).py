count = int(input("정수를 입력하시오 : "))
i = 1 # while문은 미리 변수를 작성해준다.
SUM = 0
while (i <= count):
    SUM += i
    i += 1
print("1부터 %s까지의 합은 %s입니다." %(count, SUM))
