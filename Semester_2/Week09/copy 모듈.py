### copy 모듈 ###
# copy를 사용하면 얕은복사, 깊은복사 등이 가능
# 하지만 새로 만들어진 객체들의 id는 전부 다르다.
# 즉, 얕은복사를 해도 id가 그대로 복사되지 않고 새로운 id가 부여된다.

print("### copy 모듈 사용 o, 리스트의 경우 ###")
import copy
c = [1, 2, [3, 4]] # 1,2,3,4같은 정수는 immutable, 리스트는 mutable
c1 = copy.copy(c)
c2 = copy.deepcopy(c)
print(c, c1, c2)
print(id(c), id(c1), id(c2)) # 얕은복사, 깊은복사 상관없이 전부 다른 id
c[0] = 100 # 정수형 자료 > immutable > 얕은복사를 한 c1도 안바뀐다.
print(c, c1, c2)
c[2].append(7) # 리스트 자료 > mutable > 얕은복사를 한 c1은 바뀐다.
print(c, c1, c2)
c[2][0] = 0 # 리스트 자료 > mutable > 얕은복사를 한 c1은 바뀐다.
print(c, c1, c2, "\n")

print("### copy 모듈 사용 o, 리스트가 아닐 경우 ###")
d = 'hello'
d1 = copy.copy(d)
d2 = copy.deepcopy(d)
d3 = d
print(d, d1, d2, d3)
print(id(d), id(d1), id(d2)) # 전부 id가 같다. 리스트의 경우에만 id가 다름
d = 100 # d만 바뀐다. 심지어 d3도 안바뀜
# 즉, 리스트의 경우에서만 얕은복사, 깊은복사의 개념이 제대로 정립되어 있다.
print(d, d1, d2, d3, "\n")

print("### copy 모듈 사용 x ###")
e = [1, 2, 3, 4]
e1 = e # 얕은복사
e2 = e.copy() # 깊은복사
e[0] = 100
print(e, e1, e2)
# 일반적인 리스트의 copy는 immutable도 바뀐다. copy모듈에서만 특수하다.

