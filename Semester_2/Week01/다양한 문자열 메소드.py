# 문자열.isalpha() : 모든 요소가 알파벳인지 판별 
s = 'yys'
print(s.isalpha())

# 문자열.isdigit() : 모든 요소가 숫자인지 판별 (int형 x char형 o)
a = '100'
print(a.isdigit())

# 문자열.isspace() : 모든 요소가 공백인지 판별
t = ' ' ' '
print(t.isspace())


# 문자열.count('문자열', 범위(이상), 범위(미만)) : 범위 내에서 문자열이 들어간 수
state = 'mississippi'
print(state.count('ssi'))
print(state.count('s', 1, 8))
print(state.count('s', 3))

# 문자열.find('문자열', 범위(이상), 범위(미만)) : 범위 내에서 문자열이 처음 들어간 인덱스
print(state.find('s'))
print(state.find('s', -10, -2))
print(state.find('s', 3))
print(state.find('i', 2, 5))

# 문자열.join(리스트) : 문자열을 리스트 사이사이 연결함. (리스트 -> 문자열로 변환)
a = ['ruti', 'albert', 'ark']
print(' '.join(a)) # 문자 사이에 공백 출력
b = '-'
t = b.join(a)
print(t, type(t))
print(b.join(a)) # 문자 사이에 - 출력

# 리스트.split(문자열) : 문자열을 공백 기준으로 잘라 리스트에 저장 (문자열 -> 리스트로 변환)
# 괄호 안에 문자열을 넣으면 해당 문자열 기준으로 분리
print('Yang Yun Seong'.split())
date = '2019/09/27'
print(date.split('/'))

