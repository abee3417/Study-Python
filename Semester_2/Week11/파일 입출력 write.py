import os.path # 경로를 추적하는 메소드

# outfile = open("phones.txt", "w")
# 이 문장이 여기에 있으면 파일이 처음부터 덮여씌워 지므로, if문을 사용한다.

if (os.path.isfile("phones.txt")): # phones.txt가 이미 있을 경우
    print("중복파일")
else:
    ### r 모드 메소드 ###
    # 파일객체.write("문장") : 문장을 파일에 작성
    outfile = open("phones.txt", "w") # 여기에다 작성해준다.
    outfile.write("홍길동 010-1234-5678\n")
    outfile.write("김철수 010-1234-5679\n")
    outfile.write("김영희 010-1234-5680\n")
    outfile.close()

# 문자열 메소드의 split 활용
infile = open("phones.txt", "r")
for line in infile:
    line = line.rstrip()
    wlist = line.split()
    # 문자열.split(문자) : 해당 문자를 기준으로 문자열을 분리 후 리스트로 저장
    # 아무것도 안 쓰면 공백 기준으로 저장
    for i in wlist:
        print(i)

infile.close()

# 추가 팁 : 이진 파일 읽을 때는 r대신 rb, 쓸 때는 w 대신 wb 사용
