class Car:
    def __init__(self, speed):
        self.speed = speed
    def setSpeed(self, speed):
        self.speed = speed
    def getDesc(self):
        return "차량 속도 = ({})".format(self.speed)

class SportsCar(Car):
    def __init__(self, speed, turbo):
        super().__init__(speed)
        self.turbo = turbo
    def setTurbo(self, turbo):
        self.turbo = turbo

a = SportsCar(100, True)
print(a.getDesc())
a.setTurbo(False)
print(a.getDesc())
