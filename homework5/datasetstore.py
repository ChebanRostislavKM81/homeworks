store={
    "staff":{
        "Bob":{
            "age":27,
            "sex":"Male",
            "ages at store":3},

        "Boba":{
            "age":20,
            "sex":"Female",
            "ages at store":0.5},
        "Boban":{
            "age":25,
            "sex":"Male",
            "ages at store":2},
    },
     "sector":{
         "meat":{
             "sausages":{
                 "price":50,
                 "count":"10KG"},
             "сhicken":{
                 "price":60,
                 "count":"7KG"}
                  },
         "fruits":{
             "apples":{
                 "price":10,
                 "count":"15KG"},
             "bananas":{
                 "price":10,
                 "count":"10KG"}
             }
             }
         }
#рекурсивно вывести названия секторов
#посчитать колво в секторах
icodes=list(store["sector"])
def PrintSector(icodes):
    if icodes == []:
        return None
    else:
        print(icodes[0])
        PrintSector(icodes[1:])
print(PrintSector(icodes))
def CountSector(icodes):
    if icodes == []:
        return None
    else:
        print(len(list(store[icodes].keys())))

print(PrintSector(icodes))