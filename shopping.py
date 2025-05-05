list = [["Shirt", 2500.0, "Casual"],["Jeans", 4000.0, "Denim"],["T-Shirt", 1500.0, "Sport"],["Jacket", 6000.0, "Winter"],["Cap", 800.0, "Casual"]]

#=============================
list_new=[]


#=============================
for i in range(0,len(list)):
    if list[i][2] != "Casual":
        list_new.append(list[i])
        
print(list_new)
