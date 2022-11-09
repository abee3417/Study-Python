class Car:
    def __init__(self, speed = 0, color = 'black', gear = 1):
        self.__speed = speed
        self.__color = color
        self.__gear = gear
    def setSpeed(self, speed):
        self.__speed = speed
    def setColor(self, color):
        self.__color = color
    def setGear(self, gear):
        self.__gear = gear
    def view(self):
        return print('speed = %d, gear = %d, color = %s' %(self.__speed, self.__gear, self.__color))
    def __str__(self): #출력해주는 내장함수
        return '(%d, %d, %s)' %(self.__speed, self.__gear, self.__color)
        #튜플형태로 저장

myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
myCar.view()
print(myCar)
