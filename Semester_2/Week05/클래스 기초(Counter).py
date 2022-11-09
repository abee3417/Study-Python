# 클래스는 인스턴스변수와 메소드로 구성
# 클래스 내 메소드의 첫 번째 인자는 항상 self로 시작
# 메소드 함수들은 대문자이름 잘 안붙임
# 클래스 내 변수들은 self.를 붙임
# __init__(self, 매게변수 = 숫자) : 생성자 -> 변수를 초기화하는 메소드
# 매개변수를 받았을 땐 매게변수로 초기화, 안받았으면 해당 숫자로 초기화

class Counter:
    def __init__(self, init_v = 0): 
        self.count = init_v
    def reset(self): # count를 다시 0으로 되돌림
        self.count = 0 
    def increment(self):
        self.count += 1
    def get(self):
        return self.count
        
    
a = Counter() # 매개변수x -> 0으로 초기화
a.increment() # count가 1이 늘어남
a.increment() # count가 1이 늘어남
print("a 카운터 값 : {}".format(a.get())) # count = 2
a.reset()
print("a 카운터 값 : {}".format(a.get())) # count = 0

b = Counter(100) # 매개변수100 -> 100으로 초기화
print("b 카운터 값 : {}".format(b.get())) # count = 0
