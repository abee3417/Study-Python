### 상속 ###
'''
class 자식클래스 이름(주모클래스 이름):
    생성자
    메소드
'''
class Vehicle: # 부모 클래스 Vehicle
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
    def setMake(self, make):
        self.make = make
    def getMake(self):
        return self.make
    def getDesc(self):
        return "차량 = ("+str(self.make)+","\
                        +str(self.model)+","\
                        +str(self.color)+","\
                        +str(self.price)+")"\

class Truck(Vehicle): # 자식 클래스 Truck
    def __init__(self, make, model, color, price, payload):
        # super().__init__(매개변수들) : 부모클래스의 생성자로 전달하고 받아옴
        super().__init__(make, model, color, price)
        self.payload = payload
    def setPayload(self, payload):
        self.payload = payload
    def getPayload(self):
        return self.payload
    def getDesc(self): # 부모 클래스 오버라이딩
        return "차량 = ("+str(self.make)+", 모델:"\
                        +str(self.model)+", 색상:"\
                        +str(self.color)+", 가격:"\
                        +str(self.price)+", 적재량:"\
                        +str(self.payload)+")"

def main(): # 메인 함수 정의
    a = Truck("Tisla", "S", "white", 10000, 2000)
    a.setMake("Tesla") # 자식 클래스에서 부모 클래스의 메소드 사용 가능
    a.setPayload(3000)
    print(a.getDesc())

main()
                        
