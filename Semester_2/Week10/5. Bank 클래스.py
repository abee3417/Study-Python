class BankAccount:
    def __init__(self, name, num, balance):
        self.balance = balance
        self.name = name
        self.num = num
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

class SaveAccount(BankAccount):
    def __init__(self, name, num, balance, rate):
        super().__init__(name, num, balance)
        self.rate = rate # 금리
    def setRate(self, rate):
        self.rate = rate
    def getRate(self):
        return self.rate
    def add(self): # 예금에 이자를 더하는 메소드
        self.balance += self.balance * self.rate

class CheckAccount(BankAccount):
    def __init__(self, name, num, balance):
        super().__init__(name, num, balance)
        self.withdraw_charge = 10000 # 수표 발행 수수료
    def withdraw(self, amount): # 메소드 오버라이딩
        # 수수료까지 해서 차감
        return BankAccount.withdraw(self, amount + self.withdraw_charge)

a1 = SaveAccount("양윤성", 111111, 100000, 0.05)
a1.add()
print("저축예금의 잔액 = ", a1.balance)

a2 = CheckAccount("김철수", 222222, 500000)
a2.withdraw(100000)
print("당좌예금의 잔액 = ", a2.balance)
