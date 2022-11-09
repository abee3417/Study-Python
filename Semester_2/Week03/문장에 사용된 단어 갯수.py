string = '''All\'s well that ends well.
Bad news travels fast.
Well begun is half done.
Birds of a feather flock together.'''
# 문자열에 '를 넣으려면 \'를 한다.

def process(s): # 알파벳 확인 함수
    output = ""
    for ch in s: # All's가 넘어왔다면
        if(ch.isalpha()): # 알파벳만 문자열에 추가('를 걸러준다.)
            output += ch
    return output.lower() # 대문자를 전부 소문자로 변환

words = set()
for s in string.split(): # 공백 기준으로 잘라서 리스트에 넣음
    words.add(process(s))
print("사용된 단어 갯수 : {}".format(len(words)))
print(words)
