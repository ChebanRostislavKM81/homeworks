print("Тема: Констукції керування")
print("Дано два цілих числа. Вивести найменше з них.")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a<b:
    print("Min number is",a)
elif a==b:
    print("There is no min number :( ")
elif b<a:
    print("min number is", b)
