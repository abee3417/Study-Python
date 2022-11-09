class Employee:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    def getNum(self):
        return self.num

class Manager(Employee):
    def __init__(self, name, num, bonus):
        super().__init__(name, num)
        self.bonus = bonus
    def getNum(self):
        num = super().getNum()
        return num + self.bonus
    def __repr__(self):
        return "이름 : {}, 월급 : {}, 보너스 : {}".format(
            self.name, self.num, self.bonus)

yang = Manager("양윤성", 3000000, 300000)
print(yang)
