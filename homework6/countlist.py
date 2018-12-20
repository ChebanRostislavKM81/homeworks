print("Пройтись по списку через цикл for, while, рекурсію")
list=[]
m=0
while m!="stop":
    m=input("Введіть елемент списку або stop для припинення")
    list.append(m)
list.pop()
for i in list:
    print(i)
j=0
while j<len(list):
    print(list[j])
    j=j+1
def PrintList(list):
    if list==[]:
        return None
    else:
        print(list[0])
        PrintList(list[1:])
print(PrintList(list))
