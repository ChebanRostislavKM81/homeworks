print("Вывести, сколько строений на улице")
print("Вывести, сколько строений на каждую дату дату")
file = open("files/Building_permits.csv")
list1=[]
list2=[]
list3=[]
list4=[]
data = file.read()
lines = data.splitlines()
dataset = {}
keys_str = lines[0].split(",")
for j in range(1,3323):
   values_str = lines[j].split(",")
   for i in range(0,len(keys_str)):
       dataset[keys_str[i]] = values_str[i]
   a=dataset['Street Name']
   list1.append(a)
   b=dataset['Permit Creation Date']
   list3.append(b)
for k in list1:
    summa=list1.count(k)
    list2.append(summa)
for l in list3:
    summma=list3.count(l)
    list4.append(summma)
q1=(list(zip(list1,list2)))
print(set(q1))
q2=(list(zip(list3,list4)))
print(set(q2))
file.close()