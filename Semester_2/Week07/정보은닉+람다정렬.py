class Student:
    def __init__(self, name, grade, number):
        self.__name = name
        self.__grade = grade
        self.__number = number
    def getNum(self):
        return self.__number
    def getGrade(self):
        return repr(self.__grade)
    def getName(self):
        return self.__name
    def __repr__(self):
        return repr((self.__number, self.__grade, self.__name))
    
students = [Student("양윤성", 4.3, 32192530),
            Student("강형철", 4.5, 32190103),
            Student("박범순", 4.5, 32191618)]
a = sorted(students, key = lambda x : x.getName(), reverse = False)
print(a)
