list = [["Shirt", 2500.0, "Casual"],["Jeans", 4000.0, "Denim"],["T-Shirt", 1500.0, "Sport"],["Jacket", 6000.0, "Winter"],["Cap", 800.0, "Casual"]]
#============================
list_01=[]
#============================
for i in range(len(list)-1):
    if list[i][1] < list[i+1][1]:
        list_01.append(list[i])
    elif  list[i+1][1]< list[i+2][1]:
        
    else:
        pass



print(list_01)