f1 = input("원본 파일 : ")
f2 = input("복사 파일 : ")
# 이미지는 이진파일이므로 이진파일모드 사용
infile = open(f1, "rb")
outfile = open(f2, "wb")
# 입력 파일에서 1024바이트씩 읽어서 출력 파일에 작성
while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer: # 더 이상 없으면 반복 종료
        break
    else: # 아니면 이미지를 복사
        outfile.write(copy_buffer)

infile.close()
outfile.close()
