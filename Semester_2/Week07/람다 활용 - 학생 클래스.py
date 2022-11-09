class Student:
    def __init__(self, name, grade, number):
        self.name = name
        self.grade = grade
        self.number = number
    # str함수 : 객체를 생성해서 출력하면 보여주게끔 하는 함수, 문자열
    # repr함수 : 객체를 생성해서 출력하면 보여주게끔 하는 함수, 표현식
    # 객체를 나타날 때는 repr가 더 좋다.
    def __repr__(self):
        return repr((self.name, self.grade, self.number))
    
print(str('따옴표가 없음')) # 문자열 그 자체를 출력
print(repr('따옴표가 있음')) # 묶어서 출력

a = Student('양윤성', 4.0, 32192530)
print(a)
# 이렇게 출력하면 바로 뭐가 들어있는지 알게끔 출력하는게 repr, str함수이다.
# 안쓰면 알아볼 수 없게끔 출력된다.

s = [Student('홍길동', 3.9, 20190303),
     Student('김철수', 3.0, 20190302),
     Student('최자영', 4.3, 20190301)]
print(sorted(s, key = lambda x : x.grade)) # 클래스가 리스트의 요소이므로 가능하다
