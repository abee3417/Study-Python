year = int(input("연도를 입력하세요. : "))
if (year % 100 != 0 and year % 4 == 0 or year % 400 == 0) :
    print("%s년은 윤년입니다." %year)
else :
    print("%s년은 윤년이 아닙니다." %year)
