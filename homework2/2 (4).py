print("Тема: Поняття змінної та типу даних у Python")
print("N студентів отримали K яблука і розподілити їх між собою порівну. Не поділені яблука залишились у кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?")
n=int(input("Введіть кількість студентів"))
k=int(input("Введіть кількість яблук"))
if n>k:
    print("Студенти вирішили не брати яблука")
else:
    ans=k//n
    wer=k%n
    print("Кожен студент отримав ",ans,"яблук")
    print("У кошику залишилось",wer,"яблук")