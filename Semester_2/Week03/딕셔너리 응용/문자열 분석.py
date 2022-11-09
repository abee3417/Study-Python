st = input("문자열을 입력하시오 : ")
table = {'digits' : 0, 'spaces' : 0, 'alphas' : 0} # 이렇게도 저장가능
for i in st: # 문자열의 문자 하나하나 끊어야하므로 split은 쓰지 않는다.
    if (i.isdigit()):
        table['digits'] += 1
    elif (i.isspace()):
        table['spaces'] += 1
    elif (i.isalpha()):
        table['alphas'] += 1
print(table)
