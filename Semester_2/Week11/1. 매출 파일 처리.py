# 입력 파일 이름과 출력 파일 이름을 받는다.
infilename = input("입력 파일 이름 : ")
outfilename = input("출력 파일 이름 : ")

# 입력과 출력을 위한 파일을 연다.
infile = open(infilename, "r")
outfile = open(outfilename, "w")

# 합계와 횟수를 위한 변수 정의
sum = 0
count = 0

# 입력 파일에서 한 줄을 읽어서 합계를 계산
for i in infile:
    sum += int(i)
    count += 1

# 총 매출을 작성
outfile.write("총매출 : {}\n".format(sum))
outfile.write("평균 일매출 : {}\n".format(sum/count))

infile.close()
outfile.close()
