# 리스트는 c의 배열과 달리 0번 인덱스와 리스트의 주소가 다르다.
lt = [1, 2, 3, 4, 5]
print(id(lt), id(lt[0]), id(lt[1])) # 셋 다 다르게 나온다.
print(id(1), id(2)) # 각 숫자들도 고유한 숫자를 갖고 있다.

# 빈 리스트를 만드는 방법은 두 가지가 있다.
# 리스트의 선언 방법
lt1 = []
lt2 = list()

# 리스트.append(내용) : 리스트에 내용 추가
lt1.append(1)
lt1.append(2)

# 리스트b = 리스트a.copy() : 리스트a를 b에 복사 (깊은 복사!) -> lt1과 lt2는 다른 존재
# 다른 존재이므로 서로를 바꿔도 영향이 없다.
lt2 = lt1.copy()

# 리스트b = 리스트a : 리스트a를 b에 할당 (얕은 복사!) -> lt1과 lt3은 같은 존재
# 그러므로 서로를 바꿔도 같이 바뀐다.
lt3 = lt1
lt1.append(3)
lt3.append(4)
print("lt1 : ", lt1)
print("lt2 : ", lt2)
print("lt3 : ", lt3)

# 리스트a.extend(리스트b) : 리스트b를 리스트a 뒤에 붙여 확장함
lt2.extend(lt3)
print("extend 후 결과 : ", lt2)

# 리스트.index(내용) : 해당 내용이 가장 먼저 들어있는 인덱스 번호를 알려준다.
print("3이 들어있는 인덱스는 {}번 입니다.".format(lt2.index(2)))

# 리스트.insert(인덱스번호, 내용) : 해당 인덱스 번호에 내용을 추가
lt2.insert(0, 'a')
lt2.insert(2, "my python score is a+")
print("insert 후 결과 : ", lt2)

# 리스트.pop() : 가장 마지막 인덱스번호에 들어있는 내용을 삭제한다.
# 리스트.pop(인덱스번호) : 해당 인덱스 번호에 들어있는 내용을 삭제한다.
lt2.pop()
lt2.pop(0)
print("pop 후 결과 : ", lt2)

# 리스트.remove(내용) : 해당 내용이 들어있는 가장 앞의 데이터를 삭제한다. (중복이여도 마찬가지)
lt2.remove(1)
lt2.remove("my python score is a+")
print("remove 후 결과 : ", lt2)

# 리스트.reverse() : 리스트를 반대로 정렬
lt2.reverse()
print("reverse 후 결과 : ", lt2)

# 리스트.sort() : 리스트를 오름차순으로 정렬
lt2.sort()
print("sort 후 결과 : ", lt2)

# 리스트.clear() : 리스트 초기화 (할당관계일 경우 같이 초기화)
lt3.clear()
print("clear 후 결과 : ", lt1, lt2, lt3)


