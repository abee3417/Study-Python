lt1 = [1, 2, 3, 4, 5]
lt2 = [6, 7, 8]
print(lt1 + lt2) # 리스트가 서로 붙여서 나옴
lt1.extend(lt2 * 2)
print(lt1)
### 오류 print(lt1 * lt2)
print(lt1 * 3) # 리스트가 3번 반복해서 나옴

print(3 in lt1) # 3이 lt1에 있는지 확인
print(3 not in lt1) # 3이 lt1에 없는지 확인
print(len(lt1)) # lt1의 길이

st1 = 'abc'
st2 = 'd e f'
print(st1 + st2) # 문자열이 서로 붙여서 나옴
