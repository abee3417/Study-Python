class Television:
    def __init__(self, channel = 5, volume = 10, onoff = True):
        # 이렇게 생성자를 만들면 인자가 없을 경우 기본 값을 설정할 수 있다.
        self.channel = channel
        self.volume = volume
        self.onoff = onoff
    def show(self):
        print("채널 : %s, 볼륨  %s, 전원 : %s"
              %(self.channel, self.volume, self.onoff))
    def setChannel(self, channel):
        self.channel = channel
    def getChannel(self):
        return self.channel
    def __str__(self):
        return "채널 : %s, 볼륨 : %s, 전원 : %s" %(self.channel, self.volume, self.onoff)

a = Television(11, 20)
print(a)
a.setChannel(15)
print(a)

# 순서대로 매개변수를 안 줘도 무엇을 줄지 명확히 명시하면 상관 x
b = Television(onoff = False, channel = 2)
b.show()

# 정확히 예상이 가능한 것들만 섞어서 쓸 수 있다.
# 틀린 예시 : c = Television(onoff = False, 25, volume = 30)
c = Television(25, onoff = False, volume = 30)
c.show()
