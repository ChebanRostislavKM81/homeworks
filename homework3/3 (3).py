print("Тема: Констукції керування")
print("Дано 3 цілих числа. Вивести мінімальне з цих чисел.")
a=int(input("Enter 1 number"))
b=int(input("Enter 2 number"))
c=int(input("Enter 3 number"))
if a<b and a<c:
    print("Min number is",a)
elif b<a and b<c:
    print("Min number is",b)
elif c<a and c<b:
    print("Min number is",c)
elif a==b and a<c:
    print("Min number is",a)
elif c==b and c<a:
    print("Min number is", c)
elif c==a and c<b:
    print("Min number is", c)
else:
    print("There is no min number :(")