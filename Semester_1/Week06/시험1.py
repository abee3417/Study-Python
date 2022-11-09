num1 = int(input("숫자1입력"))
num2 = int(input("숫자2입력"))
if (num1 >= num2):
    result = num1 % num2
    if (result == 0):
        result = num2
else:
    result = num2 % num1
    if (result == 0):
        result = num1
print("최대공약수는 %s" %result)
