##### 함수 정의하기 #####
def add():
    print("용인시 수지구 죽전동")
    print("단국대학교 소프트웨어-ICT관")
    print("창사코\n")

def name():
    print("양윤성")
    printtttt("창사코")
    # 에러 메세지가 안뜬다. -> name함수 호출을 안해줬기 때문이다.

def name_add1(name):
    print("용인시")
    print(name) # 파라메터를 사용

def name_add2(addr, name):
    print(addr)
    print(name)

def cal_1(r):
    area = 3.14 * r**2 # r의 제곱
    return area # 돌려주는 값이 있으면 꼭 return을 써준다.


##### 함수 호출하기 : 함수이름()를 써주면 된다. #####
add()
name_add1("양윤성\n") # 파라메터를 보내줌
name_add2("용인시", "양윤성\n\n") # 파라메터 2개를 보내줌

print(cal_1(10)) # cal_1 함수에는 print해주는게 없으므로 print를 써준다.
a = cal_1(10)
print("반지름이 10인 원의 넓이는 %s입니다." %a) # 똑같이 출력된다.
