print("Тема: Констукції керування")
print("Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним.")
a=int(input("Введіть рік"))
if a%4==0 and a%100!=0:
    print("LEAP")
elif a%400==0:
    print("LEAP")
else:
    print("COMMON")