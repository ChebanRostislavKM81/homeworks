print("Тема: Констукції керування")
print("Визначити, чи може тура перейти з першої клітини у другу за один хід.")
a1=int(input("Введіть першу координату першої клітинки"))
a2=int(input("Введіть другу координату першої клітинки"))
b1=int(input("Введіть першу координату другої клітинки"))
b2=int(input("Введіть другу координату другої клітинки"))
if a1==b1 or a1==b2:
    print("YES")
elif a1!=b1 and a2!=b2:
    print("NO")
