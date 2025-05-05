name_age=[]

def input1():
    a=input("enter your name: ")
    b=input("enter your name: ")
    name_age.append(a)
    name_age.append(b)

for i in range(0,3):
        input1()

for j in range(0,4,2):
    print(name_age[j],":",name_age[j+1])
