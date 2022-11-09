name = input("파일 이름 : ")
file = open(name, 'r')

table = dict()
# 여기서 file는 4줄이므로 문장 끝 기준 4번 반복
for line in file:
    words = line.split()
    for word in words: # 리스트의 처음부터 끝까지 반복
        if word in table: # 기존 단어면 수 증가
            table[word] += 1
        else: # 새로운 단어면 추가
            table[word] = 1
print(table)
