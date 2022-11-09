class Vehicle:
    def __init__(self, name):
        self.name = name
    def drive(self):
        raise NotlmplementedError("이것은 추상메소드입니다.") # 에러 구현
    def stop(self):
        raise NotlmplementedError("이것은 추상메소드입니다.")

class Car(Vehicle):
    def drive(self):
        return "승용차를 운전합니다."
    def stop(self):
        return "승용차를 정지합니다."

class Truck(Vehicle):
    def drive(self):
        return "트럭을 운전합니다."
    def stop(self):
        return "트럭을 정지합니다."
    
cars = [Truck("Truck1"), Car("Car1"), Car("Car2")]
# 이런 식으로 리스트 안에 객체도 저장 가능
for i in cars:
    print(i.name + ':' + i.drive())
