### tuple 선언 방법 2가지 : 소괄호를 넣어도 되고 넣지 않아도 된다.
### 단, 콤마(,)는 무조건 넣어야 한다.
### O/X문제로 내기 좋으니 충분히 숙지할 것.
t1 = (1, 2, 3)
t2 = 4, 5, 6
t3 = (1) # 콤마가 없으므로 tuple이 아닌 int 타입이다.
t4 = (1,) # True
t5 = 1, 2, 3, # True
t6 = 'a', 0.3, 2, [1,2,3], (4,5,6) # 문자, 기호, 리스트, 튜플도 튜플의 원소로 가능
t7 = t6, (4, 5, 6, 7) # 이 경우에는 괄호를 구분 -> 길이 2
t8 = t6,  4, 5, 6, 7 # 길이 5 (tuple로 인식 x)
print(type(t1), type(t2), type(t3), '\n' , type(t4), type(t5), type(t6))
print("t7의 길이 : {}, t8의 길이 : {}".format(len(t7), len(t8)))
print(type(t7), type(t8))

### tuple의 메소드 : +, *, not in, len
print("t1 + t2 : ", t1 + t2) # 문자열을 서로 붙임
print((1, 2, 3) + (4, 5, 6)) # tuple 끼리 더함
# tuple끼리 역시 더하지만 +의 우선순위가 높아서 3 + 4 = 7로 바뀌고 더한다.
print(1, 2, 3 + 4, 5, 6)


### 빈 tuple을 선언 방법도 리스트랑 비슷하다.
t1 = ()
t2 = tuple()


### tuple 심화
a, b, c = 10, 20, 30
t = 10, 20, 30
print(t)
# t에 10, 20, 30이 tuple로 들어간다.

a, b, c = t
print(a, b, c)
print(type(a)) # a는 int형
# tuple의 원소를 순서대로 하나씩 준다.
# 단, tuple의 갯수와 원소를 받을 변수의 갯수도 같아야 한다. 3개 = 3개


### 파이썬에서 swap할 때 따로 변수를 만들지 않고 가능 (tuple 원리 이용)
x = 10
y = 20
print("swap 전 : {}, {}".format(x, y))
x, y = y, x
print("swap 후 : {}, {}".format(x, y))

### 기타
# 문자열을 4번 출력
str1 = ('hi') * 4 # str1 = 'hi' * 4 와 같다.
print("str1 : ", str1, type(str1), len(str1))

# 튜플 자체를 4번 출력
str2 = ('hi',) * 4
print("str2 : ", str2, type(str2), len(str2))

# 문자열을 4번 출력한 걸 튜플에 삽입
str3 = ('hi') * 4, # str3 = 'hi' * 4, 와 같다.
print("str3 : ", str3, type(str3), len(str3))

### 오류 str4 = 'hi', * 4 hi : 튜플로 4개가 묶일것 같지만, *가 피연산자 인식을 못해서 오류난다.
### 괄호를 붙여줘야 한다. -> ('hi',) * 4

str4 = (1, 2, 3, 4, 5)
print(3 in str4) # True
print(3 in (1, 2, 3)) # 1, 2, 3 튜플에 3이 있으므로 True
### 오류 3 in 1, 2, 3 은 작동이 안되는데, in 뒤에는 하나의 argument만 와야 하기 때문이다.

for x in (1, 2, 3):
    print(x)
for x in 1, 2, 3:
    print(x)
### 둘 다 가능하다. for문은 괄호 상관 x
