import fibo
a = fibo.fib(100)
b = fibo.fib2(100)
print(a)
print(b)
c = fibo.__name__ # 모듈의 이름
d = fibo.__spec__ # 모듈의 상세내용 (위치 등)
print(c)
print(d)

fib = fibo.fib # 변수에다가 모듈 내의 함수를 삽입
print(fib(50)) # 그러면 정상작동 된다.
