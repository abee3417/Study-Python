### 집합의 연산자 ###

a = {1, 2}
b = {1, 2, 3, 4}
print("a와 b는 같은가? : %s" %(a == b)) # 동일집합 구분
print("a는 b의 부분집합? : %s" %(a.issubset(b))) # 부분집합 구분
print("a와 b의 합집합 : %s" %(a | b)) # 합집합 출력, a.union(b)와 같은 말
print("a와 b의 교집합 : %s" %(a & b)) # 교집합 출력, a.intersection(b)와 같은 말
print("a와 b의 차집합 : %s" %(b - a)) # 차집합 출력, a.difference(b)와 같은 말

print("a는 b의 부분집합? : %s" %(a.issubset(b))) # 부분집합 구분
print("a와 b의 합집합 : %s" %(a.union(b))) # 합집합 출력, a.union(b)와 같은 말
print("a와 b의 교집합 : %s" %(a.intersection(b))) # 교집합 출력, a.intersection(b)와 같은 말
print("a와 b의 차집합 : %s" %(b.difference(a))) # 차집합 출력, b.difference(a)와 같은 말
