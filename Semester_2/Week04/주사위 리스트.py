rows = 6
cols = 6
dlist = []
# 2차원 리스트 생성
for row in range(rows):
    dlist += [[0] * cols]
# 각 칸마다 (행+1) + (열+1)을 한다. (리스트는 0,0 시작이므로)
for row in range(rows):
    for col in range(cols):
        dlist[row][col] = (row + 1) + (col + 1)
print(dlist)
