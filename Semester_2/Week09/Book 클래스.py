class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages
    def __str__(self):
        return self.title
    

b1 = Book("자료구조", 600)
b2 = Book("c언어", 700)
print(b1 + b2)
print(b1)
