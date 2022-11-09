class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "알 수 없음"

class Dog(Animal): # 딱히 생성자가 필요없으므로 super() x
    def speak(self): # 메소드 오버라이딩
        return "멍멍"

class Cat(Animal):
    def speak(self):
        return "야옹"

alist = [Dog("Albert"), Dog("Ruby"), Cat("Ruti")]
for i in alist:
    print("{} : {}".format(i.name, i.speak()))
    # 똑같은 speak 명령이지만 다른 결과가 나온다. > 다형성
