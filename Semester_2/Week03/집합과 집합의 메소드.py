### 집합의 개념과 메소드 ###
'''
- 중괄호 {}로 표현
- 중복이 되면 안된다.
- 순서가 없다. (s1[0] 처럼 인덱스 사용 불가!)
- in, not in, len 사용 가능
'''

s1 = {5, 4, 3, 2, 1, 5, 1, 1}
s2 = set() # 빈 집합
s3 = {} # 중괄호만 쓰면 집합이 아닌 딕셔너리로 생성된다.
s4 = {100} # 원소 하나가 있는 집합

print(2 in s1)

print(s1)
# 반복문을 사용할 땐 집합을 오름차순으로 정렬해준다.
for x in s1:
    print(x, end = ' ')
print('\n')  
for x in {1, 3, 2}:
    print(x, end = ' ')
print('\n')
# 집합.add(원소) : 순서 상관없이 랜덤으로 집합에 원소를 추가한다.
s4.add(50)
print("add 이후 s4 : {}".format(s4))
# 집합.clear() : 공집합으로 만든다.
s4.clear()
print("clear 이후 s4 : {}".format(s4))
# 집합.copy() : 집합 복사
s4 = s1.copy()
# 집합.discard(원소) : 해당 원소를 전부 삭제 (없는 원소 삭제 시 오류x)
s4.discard(5)
# 집합.remove(원소) : 해당 원소를 전부 삭제 (없는 원소 삭제 시 오류발생)
s4.remove(4)
print("copy, discard, remove 이후 s4 : {}".format(s4))
# 집합.pop() : 랜덤으로 집합의 원소 중 하나를 가져오고 삭제
# 리스트와 튜플과는 달리 pop안에 아무것도 쓰면 안된다. (인덱스 사용 불가)
s4.pop()
print("pop 이후 s4 : {}".format(s4))
