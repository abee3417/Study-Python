# abs(숫자) : 절댓값
print(abs(-1))
# chr(숫자) : 숫자->아스키코드
print(chr(65))
# ord(문자) : 아스키코드->숫자
print(ord('a'))
# dir(객체) : 객체 안에서 사용 가능한 메소드를 알려줌
dir([1, 2])
# eval(문장) : 해당 문장 실행 (수식도 가능)
print(eval("1+2"))
print(eval("print('Hi!')")) # 물론 print도 출력됨 -> Hi! 출력
# exec(문장) : 해당 문장 실행 (eval이랑 다르게 리턴값 x)
print(exec("1+3")) # 그래서 아무것도 실행이 안된다.
exec("x = 1 + 3")
print(x) # 그래서 이런식으로 해야한다.
s = '''
import math
def c_area(r):
    return math.pi * r * r
'''
exec(s)
print(c_area(5)) # 이런식으로도 exec활용이 가능
# list(문자열) : 문자열을 리스트로 하나씩 끊어서 저장
x = list("YYS")
print(x)
# max/min(리스트/튜플/문자열) : 가장 큰 값/가장 작은 값 출력
print(max('abcde'))
print(min('0468912'))
# sorted(리스트/튜플/문자열) : 리스트를 정렬함 (원본 변경 x)
# 딕셔너리를 sorted하면 키값만 정렬
print(sorted((7, 1, 5, 3)))
print(sorted("The Albert know not of its health")) # 알파벳 단위로 정렬
print(sorted("The Albert know not of its health".split())) # 단어 단위로 정렬
print(sorted("The Albert know not of its health".split(), key = str.lower)) # + 소문자 대문자 구별x
# 리스트.sort() : 리스트 원본 자체를 정렬
