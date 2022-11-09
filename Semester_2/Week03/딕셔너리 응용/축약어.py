lib = dict()
lib["B4"] = "Before"
lib["TX"] = "Thanks"
lib["BBL"] = "Be Back Later"
lib["BCNU"] = "Be Seeing You"
lib["HAND"] = "Have A Nice Day"
st = input("번역할 문장을 입력하시오 : ")
st = st.split()
result = ""
for i in st:
    if i in lib: # 입력한 문장이 lib에 있을 때
        result += lib[i] + " " # 해당 딕셔너리 출력
    else: # 없으면
        result += i + " " # 그대로 출력
print(result)
