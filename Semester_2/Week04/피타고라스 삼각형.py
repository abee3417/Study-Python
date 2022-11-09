# 함축 사용 x
olist = []
for x in range(1, 30):
    for y in range(x, 30):
        for z in range(y, 30):
            if x**2 + y**2 == z**2:
                olist.append((x, y, z))
print(olist)

# 함축 사용 o
# 함축에 for문을 여러번 사용할 땐 순서대로 작성한다.
nlist = [(x, y, z) for x in range(1, 30) for y in range(x, 30)
         for z in range(y, 30) if x**2 + y**2 == z**2]
print(nlist)
