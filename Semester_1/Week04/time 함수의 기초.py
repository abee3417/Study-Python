## time 함수 ##
import time

now = time.time()
# time.time()을 사용하면 1970년 1월 1일 이후부터 흐른 시간을 초단위로 출력
thisyear = int(1970 + now//(365 * 24 * 3600))
# 1년, 하루 24시간, 1시간 3600초를 곱하고 1970을 더해주면 올해가 나온다.
# int로 계산값을 감싸줘야 소숫점 출력이 되지 않는다.

print("올해는 %s년 입니다." %thisyear)
age = int(input("몇살이신지요? "))
print("2050년에는 %s살 이시군요." %(age + 2050 - thisyear))
