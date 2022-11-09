# 파이썬에서 문장의 표현은 " " 아니면 ' ' 를 사용한다.
# msgX = "hello'
# Error : 큰 따옴표와 작은 따옴표는 안된다.
msgO = 'hello'

msg1 = "i'm a boy"
msg2 = 'he said, "i am happy."'

n1 = int('100') * 3
n2 = int(100.5) * 3

# numX = int("100.5") * 3
# Error : 문자->실수->정수 이렇게 변환은 안된다.
numO = float("100.5") * 3

f1 = float(100) * 3
f2 = float("100") * 3 # 문자->정수->실수 변환은 가능 (메모리의 개념)

print(msgO)
print(msg1)
print(msg2)
print(n1)
print(n2)
print(numO)
print(f1)
print(f2)
