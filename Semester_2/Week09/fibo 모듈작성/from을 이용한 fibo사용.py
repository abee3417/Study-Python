# fibo 모듈로부터 fib함수만 가져오고 싶을 때 : from a import b
# import 옆에는 몇 개든 상관x : ex) from a import b, c, d
from fibo import fib

# 만약 from fibo import * 를 하면 fibo 내의 함수를 모두 가져온다.
# fibo.fib2 말고 그냥 fib2만 써도 함수 사용이 가능하단 강점때문에 사용한다.

print(fib(10))
# 즉, 현재는 import fib만 했기에 fibo 내에 있는 fib2는 안된다.
