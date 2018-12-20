print("Тема: Констукції керування")
print("Дано три цілих числа. Визначте, скільки з них дорівнюють один одному.")
a=int(input("Enter 1 number"))
b=int(input("Enter 2 number"))
c=int(input("Enter 3 number"))
if a==b and b==c:
    print(3)
elif a==b and b!=c:
    print(2)
elif a==c and c!=b:
    print(2)
elif b==c and c!=a:
    print(2)
else:
    print(0)