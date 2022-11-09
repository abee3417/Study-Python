# print 속의 문장을 입력할 때 데이터 타입 상관없이 %s를 사용하고 뒤에 %( )로 변수로 한번에 묶어준다.
# 사용 예시1 : print("%s" %(변수))
# 사용 예시2 : print("%s %s" %(변수, 변수))
# c와 비교  : printf("%c %d", char타입 변수, int타입 변수)
price = 1000
count = 3
print("새우깡의 가격은 %s원입니다." %price)
print("새우깡 %s개의 가격은 %s원입니다." %(count, price * 3))
# price * 3처럼 변수값 변경도 바로바로 가능하다.
