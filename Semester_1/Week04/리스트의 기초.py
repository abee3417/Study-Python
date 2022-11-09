# 리스트 사용법 : slist = ['이름1', '이름2', '이름3', '이름4']
# slist[0]를 출력하면 '이름1', slist[2]를 출력하면 '이름3'을 출력
# 공백은 중괄호 안에 아무것도 안넣으면 된다. (slist = [])
xlist = []
print(xlist)
# 공백 리스트 안에 값을 넣으려면 .append(넣고싶은값) 을 사용하면 된다.
# 이때 리스트의 값은 정수형, 문자형 상관 없이 넣을 수 있다.
slist = [13, 'a', 10.2]
print(slist)
slist.append("string")
print(slist)
# 리스트 안에 또 리스트를 넣을수있다.
doublelist = [1, 2, 3]
doublelist.append([4, 5])
print(doublelist)
print(doublelist[3])
