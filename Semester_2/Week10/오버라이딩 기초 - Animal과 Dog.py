### 오버라이딩 ###
class Animal:
    def __init__(self, name = ""):
        self.name = name
    def eat(self):
        print("동물이 먹고 있습니다.")

class Dog(Animal):
    def __init__(self, name = ""):
        super().__init__()
    def eat(self): # 부모의 메소드 오버라이딩 -> 수정
        # 이렇게 하면 같은 eat을 호출했을때
        # 부모 클래스의 eat이 아닌 자식 클래스의 eat이 호출된다.
        print("강아지가 먹고 있습니다.")
        
d = Dog()
d.eat() # 여기서 eat은 자식 클래스의 소유로 친다.
