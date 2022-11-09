# 정보은닉
# 인스턴스 변수에 self.__변수이름 -> 언더바 2개를 붙인다.
# 그러면 객체명.인스턴스변수명 이런식으로 바꾸지 못하게 막는다.
# 객체명.__인스턴스변수명도 안됨

class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def bark(self):
        # 정보은닉 시 모든 변수이름을 잊지말고 바꿔주자
        print(self.__name, "is barking. ")
    # 접근자 : get + 인스턴스변수이름 -> 변수값을 리턴하는 메소드
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    # 설정자 : set + 인스턴스변수이름 -> 변수값을 설정하는 메소드
    def setName(self, name):
        self.__name = name
    def setAge(self, age):
        self.__age = age
        
x = Dog("Albert", 3)
x.bark()
print("이름 :", x.getName() + ", 나이 :", x.getAge())
x.setAge(10)
print("나이 :", x.getAge())
x.setName("Ruby")
x.bark()
