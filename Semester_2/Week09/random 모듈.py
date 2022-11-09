import random

# random.randint(이상, 이하) : 범위 내 숫자 중 하나를 가져옴
# random.random() : 0과 1 사이의 난수 중 하나를 가져옴
a = random.randint(1, 6)
b = random.random()
print(a)
print(b)

# random.choice(자료이름) : 자료 내 랜덤으로 요소 선택
c = [4, 5, "hi"]
print(random.choice(c))

mlist = [[x] for x in range(10)]
print(mlist)
# random.suffle(리스트이름) : 리스트 내부를 랜덤으로 섞는다.
random.shuffle(mlist)
print("셔플 후 : ", mlist)

# random.randrange(이상, 미만, step) : 범위 내 랜덤 출력
for i in range(3):
    a = random.randrange(0, 9, 2)
    print(a)
