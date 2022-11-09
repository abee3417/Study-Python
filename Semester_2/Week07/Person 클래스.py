class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return repr((self.name, self.age))
        return "<이름 : %s, 나이 : %s>" %(self.name, self.age)

def keyAge(person):
    return person.age

s = [Person('홍길동', 20),
     Person('김철수', 35),
     Person('최자영', 38)]
print(s)
print(sorted(s, key = lambda x : x.age))
# print(sorted(s, key = keyAge))
