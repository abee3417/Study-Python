### has-a 관계 : 객체 합성 ###
'''
구성 요소로서 : 진한 마름모
집합 관게로서 : 투명한 마름모
'''
class Animal(object): #object 안넣어도됌.
    pass # 아무것도 안 쓸 경우
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

dog1 = Dog("알버트")
person1 = Person("홍길동")
person1.pet = dog1 # 이것이 has-a 관계
# 객체의 인스턴스 변수로 다른 객체를 넣는다.
print(dog1.name, person1.name, person1.pet)
# 이렇게 하면 다른 클래스로 접근 가능.
# person1.pet = person1.pet.name
