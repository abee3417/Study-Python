infile = open("proverbs.txt", "r")
wlist = {}

# 파일의 각 줄에 대하여 문자를 추출한다. 각 문자를 사전에 추가한다.
for line in infile:
    for char in line.strip(): # 문장 양쪽 개행문제 제거
        if char in wlist: # 단어가 이미 있으면
            wlist[char] += 1 # 증가
        else: # 단어가 없으면
            wlist[char] = 1 # 추가
print(wlist)
infile.close

# 추가 팁 : strip()은 양쪽 공백 제거, rstrip()은 오른쪽, lstrip()은 왼쪽
