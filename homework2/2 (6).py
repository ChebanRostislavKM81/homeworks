print("Тема: Поняття змінної та типу даних у Python")
print("Школа вирішила сформувати три нові групи учнів та надати їм окремі класи. У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів. Яку мінімальну кількість столів необхідно придбати?")
a1=int(input("Введіть кількість учнів в 1 групі"))
a2=int(input("Введіть кількість учнів в 2 групі"))
a3=int(input("Введіть кількість учнів в 3 групі"))
if a1%2==0:
    b1=a1//2
else:
    b1=(a1//2)+1
if a2 % 2 == 0:
    b2 = a2 // 2
else:
    b2 = (a2 // 2) + 1
if a3%2==0:
    b3=a3//2
else:
    b3=(a3//2)+1
S=b1+b2+b3
print("Школі потрібно закупити",S,"парт")