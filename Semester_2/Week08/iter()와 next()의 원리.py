# 클래스 객체를 iterator로 만들고 싶을 때,
# __iter__() 와 __next__() 메소드를 만들어 준다.
class MyCounter():
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # 이터레이터 객체로서 자기 자신을 반환
    def __iter__(self):
        return self

    def __next__(self):
        # current가 high보다 크면 StopIteration
        # current가 high보다 작으면 다음 값을 반환한다
        if (self.current > self.high):
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

a = MyCounter(1, 10)
for i in a: # c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(i, end = ' ')
print("\n")

b = MyCounter(1, 10)
next(b)
next(b)
for i in b: # next를 2번 해주었기 때문에 1이 아닌 3부터 출력된다.
    print(i, end = ' ')
print("\n")
