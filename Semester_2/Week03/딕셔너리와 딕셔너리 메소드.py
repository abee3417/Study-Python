### 딕셔너리 ###
'''
- 순서 개념이 없다.
- 키값은 중복이 되지 않는다.
- 키값은 정수, 실수, bool, 복소수, 문자열, 튜플까지 가능하다. (리스트, 집합은 x)
- 저장할 내용에는 무엇이 들어가든 상관 없다.
- in, not in 사용 가능

'''
# 빈 딕셔너리 만들기
d1 = {}
d2 = dict()

# 딕셔너리 변수 = {키값 : 저장할 내용}
d3 = {'K':'01011112222', 'P' : '01033334444'}

print(d3)
print(d3['K'])
#인덱스 번호는 안되지만 인덱스의 키값으로 추적 가능
print(d3.get('A', '없음'))
print(d3.get('K', '없음'))
print(d3.get('K'))
print(d3.get('A'))
#인덱스랑 똑같은 기능이지만 해당 값이 없어도 에러x, 없으면 뒤에 문자열을 출력
print('K' in d3)
print(1 in {1:10, 2:20})

# for문에 딕셔너리를 넣으면 키값만 나옴.
for i in d3:
    print(i, end = ' ')
print('\n')
# 다 같이 출력하려면 딕셔너리.items()를 붙인다.
for i in d3.items():
    print(i, end = ' ')
print('\n')

### 딕셔너리 메소드 ###

# claer(), copy() 사용 가능
print(d3.keys()) # 키값만
print(d3.values()) # 내용만

# 내용추가 or 내용수정
d3['A'] = '01012345678'
d3['B'] = '01011111111'
d3['C'] = '01022222222'
print(d3)
# update.(변수 = '내용') -> 여기서는 키값에 따옴표를 붙이지 않는다. 이 경우는 문자열 변수일때만 가능
d3.update(YYS = '01054373899')
d3.update({'A':'01000000000'})
print("update 후 d3 : %s" %(d3))

# 내용 삭제
d3.pop('B')
del d3['C']
print(d3)

# 키값이 정수일때는 다음과 같이 한다.
d4 = {1:10, 2:20, 3:30}
d4.update({1:100})
d4['a'] = 40
d4.update({6:60})
print(d4)
# fromkeys : 리스트의 내용을 딕셔너리에 저장
l1 = [10, 20, 30]
d5 = dict()
d5 = d5.fromkeys(l1) # None으로 할당
print(d5)
d5 = d5.fromkeys(l1, 1000) # 1000으로 할당
print(d5)
