# 동적으로 2차원 리스트 생성
rows = 3
cols = 5
s = []
for row in range(rows):
    s += [[0] * cols]
    # 한 '행'마다 0을 '열'만큼 넣어준다.
for row in range(rows):
    s.append([0] * cols)

print(s)
