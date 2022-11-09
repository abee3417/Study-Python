class Person:
    def __init__(self, name, num):
        self.name = name
        self.num = num

class Student(Person):
    def __init__(self, name, num, gpa):
        super().__init__(name, num)
        self.gpa = gpa
        self.classes = []
    def setGpa(self, gpa):
        return self.gpa
    def enrollCourse(self, course):
        self.classes.append(course)
    def __str__(self):
        return "이름 : {}, 주민번호 : {}, 수강과목 : {}, 평점 : {}".format(
            self.name, self.num, self.classes, self.gpa)

class Teacher(Person):
    def __init__(self, name, num):
        super().__init__(name, num)
        self.courses = []
        self.salary = "3백만"
    def assignTeaching(self, course):
        self.courses.append(course)
    def __str__(self):
        return "이름 : {}, 주민번호 : {}, 강의과목 : {}, 월급 : {}".format(
            self.name, self.num, self.courses, self.salary)

yang = Student("양윤성", "32192530", 4.0)
yang.enrollCourse("대학기초SW입문")
print(yang)

kim = Teacher("김철수", "123456790")
kim.assignTeaching("Python")
print(kim)
