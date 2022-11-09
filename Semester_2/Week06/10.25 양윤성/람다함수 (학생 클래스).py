students = [
    ('홍길동', 3.9, 20191025),
    ('김철수', 3.0, 20191031),
    ('최자영', 4.3, 20181231),
    ('양윤성', 4.1, 20190721)]
print(sorted(students, key = lambda s : s[0], reverse = True))
print(sorted(students, key = lambda s : s[1], reverse = True))
print(sorted(students, key = lambda s : s[2], reverse = False))
