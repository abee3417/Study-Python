money = int(input("투입할 돈 : "))
price = int(input("물건 값 : "))
change = money - price

coin500 = change // 500
# 500으로 나누어서 몫 = 500원짜리의 갯수
change %= 500
# 남은 거스름돈에서 500원짜리를 전부 걸러낸다. -> 나머지를 활용
coin100 = change // 100
change %= 100
coin50 = change // 50
change %= 50
coin10 = change // 10
change %= 10

print("500원 동전의 개수 :", coin500)
print("100원 동전의 개수 :", coin100)
print("50원 동전의 개수 :", coin50)
print("10원 동전의 개수 :", coin10)
