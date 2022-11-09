'''
print(x)는 print(x, end = '\n')이랑 같은거, 즉 end가 생략된 것
그러므로 print(x, end = '문자열')을 하면 출력한 변수 뒤에 문자열이 입력된다.

for문에서 사용하는 괄호없는 리스트는 사용 가능하다.
단, 1 in 1, 2, 3이나 'ss' , * 3 이런건 안된다.
'''

#예제
for s in 1, 2, 3:
    print(s, end = ' ')
print('\n')

l1 = [10, 20, 30, 40]
print(l1, type(l1))
t1 = tuple(l1) # 리스트를 튜플로 변환
print(t1, type(t1))
