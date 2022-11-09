def check(s):
    low = 0
    high = len(s) - 1
    while True:
        if low > high: # 커지는 순간 비교 할 필요 x (중복)
            return True
        a = s[low]
        b = s[high]
        if a != b: # 같지 않을 순간 False 리턴
            return False
        
        # 똑같으면 다음 순서로 넘어감
        low += 1
        high -= 1


s = input("문자열을 입력하시오: ")

# 문자열.replace(문자1, 문자2) # 문자1 대신 문자2를 쓴다.
s = s.replace(" ", "") # 띄어쓰기를 붙인다.

if check(s) == True: # == True 없어도 된다.
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
