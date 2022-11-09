class TV:
    serialNumber = 0 #정적변수(클래스멤버), 전체 객체를 통틀어 하나만 생성
    def __init__(self, channel = 11, volume = 9):
        TV.serialNumber += 1 #정적변수를 수정할 땐 클래스명을 붙인다.
        self.channel = channel
        self.volume = volume

a = TV()
print(a.serialNumber)
b = TV()
print(b.serialNumber)
a.serialNumber = 100
#정적변수를 수정한것 같지만 이는 변수를 따로 추가한 것
print(b.serialNumber)
#그래서 b.serialNumber은 그대로 2
c = TV()
print(a.serialNumber)
#c를 새로 만들어도 a는 그대로 100
print(b.serialNumber)
#하지만 b.serialnumber은 그대로 정적변수이므로 3
TV.serialNumber = 1000
#'클래스이름.정적변수이름' 하면 serialNumber가 아직 정적변수인 b, c는 1000으로 바뀜
#a는 바뀌지 않음
print(c.serialNumber)
print(a.serialNumber)
d = TV()
#하나가 더 추가되었으므로 1000 + 1
print(b.serialNumber)
