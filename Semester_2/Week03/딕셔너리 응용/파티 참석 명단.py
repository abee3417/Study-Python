partyA = input("파티 A 명단 : ")
partyB = input("파티 B 명단 : ")
pA = set()
pB = set()

for i in partyA.split():
    pA.add(i)
for i in partyB.split():
    pB.add(i)
    
print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.\n{}".format(pA & pB))
print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.\n{}".format(pA.intersection(pB)))
