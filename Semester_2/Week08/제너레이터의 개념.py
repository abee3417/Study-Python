### 제너레이터 ###
# 제너레이터는 키워드 yield를 사용해서 함수로부터 이터레이터를 생성하는 방법
# 여기서는 next 메소드를 사용할 수 없다.
'''
 *** 이터레이터와의 차이점 ***
이터레이터는 클래스를 이용하여 이터러블 객체생성
제너레이터는 함수를 이용하여 이터러블 객체 생성
'''

def myG():
    yield 'first'
    yield 'second'
    yield 'third'

for i in myG():
    print(i, end = " ")
print("\n")

def myG2(start, end):
    while (start <= end):
        yield start
        start += 1
        
for i in myG2(0, 10):
    print(i, end = " ")
print("\n")
