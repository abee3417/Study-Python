### 이터레이터 ###
# 값을 하나씩 차례대로 반환 가능한 객체
# 이터러블 객체 : 문자열, 리스트, 튜플, 셋, 딕셔너리, 파일 전부 가능
# iterator을 리턴할 수 있는 객체
# iterable 하다고 해서 iterator하다고 할 순 없다.

# 방법1 : for문 사용
x = [1, 2, 3]
for i in x:
	print(i, end = " ")
print("\n")

# 방법2 : iter()함수 사용
# iter() : iterator 객체를 생성할 수 있음
# next() : 다음 반복을 위한 값을 반환, 더 이상의 값이 없으면 StopIteration 출력
print("iter 전 :", type(x))
x = iter(x)
print("iter 후 :", type(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x)) # 3초과 : StopIteration
