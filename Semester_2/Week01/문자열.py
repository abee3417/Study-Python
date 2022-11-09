# 문자열  출력 : 변수명[이상, 미만, 몇칸씩?]
st = 'Hello World'
print(st[0:4]) # 'Hell'
print(st[:5]) # 'Hello' 아무것도 안 쓰면 처음부터 출력한다.
print(st[6:]) # 'World' 아무것도 안 쓰면 끝까지 출력한다.
print(st[::3]) # 'HlWl' 처음부터 끝까지 출력 + 3칸씩 출력
print(st[-5:]) # 'World' 음수는 반대로 생각한다.
print(st[::-1]) # 'dlroW olleH' 칸 수에 음수로 붙일 시 반대로 출력
print(st[-1:-10:-2]) # 'drWol' 반대로 출력할 시 숫자를 반대로 입력한다.print(st[5%2]) # print(st[1]) : 'e'
print(st.upper()) # 모두 대문자로 > 'HELLO WORLD'
print(st.lower()) # 모두 소문자로 > 'hello world'
