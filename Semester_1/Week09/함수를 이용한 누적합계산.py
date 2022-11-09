def get_sum(start, end):
    sum1 = 0
    for i in range(start, end + 1):
        sum1 += i
    return sum1

start = int(input("누적합을 구할 시작값 : "))
end = int(input("누적합을 구할 종료값 : "))
total = get_sum(start, end)
print("%s부터 %s까지의 누적합은 %s입니다." %(start, end, total))

