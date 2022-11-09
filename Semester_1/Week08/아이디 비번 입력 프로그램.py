ID = "ilovepython"
PW = "password"
errorCount = 0
while (True): # while True : 무한루프
    userID = input("아이디를 입력하시오 : ")
    if (userID == ID):
        break # break를 사용하면 반복문 탈출
    else:
        print("아이디를 찾을 수 없습니다.\n")

while (True):
    userPW = input("\n비밀번호를 입력하시오 : ")
    if (userPW == PW):
        print("\n%s님, 환영합니다." %userID)
        break
    else:
        print("비밀번호 입력 오류입니다. 5회이상 틀릴 시 프로그램이 종료됩니다.\n")
        errorCount += 1
        
    if (errorCount >= 5):
        print("프로그램이 종료됩니다.")
        break
