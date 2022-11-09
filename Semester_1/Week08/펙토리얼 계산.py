count = int(input("정수를 입력하시오: "))
result = 1
for i in range(1, count + 1): # 끝값은 포함 안되므로 +1을 해준다.
    result *= i
print("%s!은 %s이다." %(count, result))
