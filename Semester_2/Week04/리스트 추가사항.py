# 리스트.sort() : 리스트를 오름차순으로 정렬 (영구히)
# sorted(리스트) : 리스트를 오름차순으로 정렬 (일시적)
lt1 = [1, 5, 3, 10, 7]
lt2 = [9, 8, 3, 6, 2]
lt1.sort()
print(lt1)
print(sorted(lt2))
print(lt2)

# 문자.join(리스트) : 해당 문자를 리스트 사이사이에 집어넣어 문자열을 만든다.
# 숫자x, 문자열로만 구성된 자료구조면 모든 가능 (튜플, 집합 등)
lt3 = ['a', 'b', 'c', 'd']
print(' '.join(lt3))
s1 = {'a', 'b', 'c', 'd'}
print('-'.join(s1))

# 리스트 함축 : 리스트 = [출력식, 변수의 범위, 조건] (실제로 콤마 안들어감)
# lt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 입력하기 어려우므로 식을 이용함.
lt4 = [x for x in range(10)] # 0~9
lt5 = [x**2 for x in range(10)] # 0의제곱 ~ 9의제곱
lt6 = [x for x in range(10) if x % 2 == 0] # 0 ~ 9중 짝수만
print(lt4)
print(lt5)
print(lt6)

# 제곱수 중 3의배수 표현 : 리스트 함축 사용
lt7 = [x**2 for x in range(10) if x % 3 == 0]

# 제곱수 중 3의배수 표현 : 리스트 함축을 사용x
lt8 = []
for x in range(10):
    if x % 3 == 0:
        lt8.append(x**2)
        # lt8 += [x**2]
print(lt7)
print(lt8)

# 2차원 리스트
s = [[1,2,3,4,5], [6,7,8,9,10]]
'''
1 2 3 4 5
6 7 8 9 10
'''
print(s[0][2]) # 3 출력
