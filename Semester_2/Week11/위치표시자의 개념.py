### 위치표시자 ###
# 사용목적 : 위치표시자를 조작하면 파일을 원하는 임의의 위치에서 읽을 수 있음.

# 새 파일의 경우
'''
위치표시자의 값이 0
'''
# 기존 파일의 경우
'''
- a모드일 경우엔 파일의 끝
- 그 외 다른 모드들은 파일의 시작 부분을 가리킴
'''
# 파일객체.seek(n) : 위치표시자를 n만큼 떨어진 곳으로 이동 (n은 바이트, n 뒤에 0 생략)
# 즉, seek(n, 0)도 상관x, seek(n, k)는 불가능
# seek은 글자 수가 아니라 바이트만큼 이동이다! (예를 들어, 한글은 한 글자당 2바이트)
# 파일객체.tell() : 현재 위치표시자의 위치를 리턴 (이것도 바이트 기준)

# 예시 : 현재 test1.txt에는 "내용\n나는 student of Dankook University." 가 적혀있다.
# 개행문자는 2바이트 (\ + n) 그러나 한글과는 다르게 중간 위치를 입력해도 오류는 x

infile = open("test1.txt", "r+")
a = infile.read(10) # 글자 수를 10개 가져옴
print("읽은 문자열 : ", a)
position = infile.tell() # 바이트 기준이라 10이 아닌 15를 출력
print("현재 위치 : ", position)
position = infile.seek(8) # 커서를 '는' 앞으로 옮긴다.
b = infile.read()
print("다시 읽은 문자열 : ", b)
infile.close()
