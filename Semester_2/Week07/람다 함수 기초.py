# 람다 -> lambda 인자리스트 : 표현식
x = 10
f = lambda x : x**2
# 람다함수는 이렇게 변수에 저장이 가능. 이때 변수는 함수가 된다.
print(type(f))
print(f(10)) # 100 출력
t = lambda x, y : x * y
print(t(2, 3))
'''
k = lambda x, y : x * y는
def k(x, y):
    return x * y 랑 같다.
'''
s = [('홍길동', 3.9, 20190303),
    ('김철수', 3.0, 20190302),
    ('최자영', 4.3, 20190301),
    ('양윤성', 4.1, 20190721)]
# (0번인덱스 : 이름, 1번인덱스 : 학점, 2번인덱스 : 학번)
print(sorted(s)) # 일반적인 경우 맨 앞인 이름 기준으로 정렬
# 학점을 정렬하고 싶을 때 key값을 사용 (튜플은 인덱스사용 가능)
print(sorted(s, key = s[1])) # def k(x) : return x[1]
print(sorted(s, key = lambda x : x[1])) # def k(x) : return x[1]
print(sorted(s, key = lambda x : x[1], reverse = True)) # 역순 정렬
# reverse 변수 : 부울형, True는 내림차순, False는 오름차순(False는 안써도됨)
