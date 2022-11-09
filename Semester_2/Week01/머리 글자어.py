s = input("문자열을 입력하시오: ")
acronym = "" # 예비 문자열
for word in s.upper().split():
# s를 대문자로 바꾸고 공백을 기준으로 자른다.
# word 리스트 0번째부터 [DAN, KOOK, UNIVERSITY] -> 2번째까지 출력
    acronym += word[0] # 차례대로 리스트에 집어넣는다.

print(acronym)
    
