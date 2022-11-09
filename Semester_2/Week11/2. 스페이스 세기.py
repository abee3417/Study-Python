def parse_file(path):
    infile = open(path)
    spaces = 0
    tabs = 0
    for i in infile:
        spaces += i.count(' ')
        tabs += i.count('\t')
    infile.close()
    
    return spaces, tabs

name = input("파일 이름 입력 : ")
spaces, tabs = parse_file(name)
print("스페이스 수 : {}, 탭의 수 : {}".format(spaces, tabs))
