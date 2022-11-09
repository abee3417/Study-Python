# 디폴트 인수 : 함수의 매개변수가 기본값을 가질 수 있다. 이걸 디폴트 인수라고 한다.
def greet(name, msg = "별일없죠?"):
    print("안녕 %s, %s" %(name, msg))
greet("윤성")


# 키워드 인수 : 인수의 이름을 명시적으로 지정해서 전달
def cal(x, y, z):
    return x - y + z

print(cal(10, 20, 30))
print(cal(x = 10, y = 20, z = 30))
print(cal(z = 30, x = 10, y = 20))
print(cal(10, z = 30, y = 20))
#print(cal(x = 10, 20, 30))
# 즉, 파라메터를 한번 지정하면 그 이후도 꼭 지정해줘야한다.
# (처음엔 안하다가 나중에 하는건 상관x)
