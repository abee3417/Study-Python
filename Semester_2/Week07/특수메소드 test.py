x = 10
y = 10
z = 20
print(x.__add__(y))
print(x.__sub__(z))
print(x.__mul__(z))
print(z.__truediv__(x))
print(z.__floordiv__(x)) # 실수 형태로 저장
print(z.__mod__(x))
print(z.__divmod__(x)) # 튜플 형태로 저장
print(x.__pow__(2))
# 크기비교 : True/False
print(x.__le__(y))
print(x.__lt__(y))
print(x.__ge__(z))
print(z.__gt__(y))
print(x.__eq__(y))

print(abs(-1))
print(chr(65))
print(ord('A'))
print("""""""""""""""""""""""""")
eval("print([x for x in range(10)])")
exec("a = [x for x in range(10)]")
print(a)
print("""""""""""""""""""""""""")

print(int("12"))
print(float(12.345))
print(list("helloworld"))
print(max({'c':100, 'b':200}))
print(min([1, 2, 3, 4, 5]))
