# sorted(리스트) : 1회성 정렬, sort() : 영구히 정렬 #
lt1 = [5, 1, 7, 2, 4]
print(sorted(lt1)) # 정배로 정렬 (1회성)
print(lt1)
lt1.sort() # 정배로 정렬 (영구성)
print(lt1)
dic1 = {3:'a', 1:'c', 5:'t', 2:'r'}
print(dic1)
print(sorted(dic1)) # key값 기준으로 정렬 (1회성)

# 만약 변수 = sorted(딕셔너리) 하면 해당 변수는 딕셔너리타입이 아닌 리스트가 된다.
a = sorted(dic1)
print(a)
print(type(a))

# 문자열도 정렬 가능
print(sorted("The health know not of their health."))
# split() : 공백 기준으로 정렬 (대문자 우선출력)
print(sorted("The health know not of their health.".split()))
a = "The health know not of their health."
# 이때, 원하는 정렬 옵션이 있을 경우 key를 사용한다. -> 문자열들을 소문자로 변환
print(sorted(a.split(), key = str.lower))
