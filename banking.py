#file=open("sampil.txt","r")
#print(file.read())
balance=500000
print("======banking=======")
start =input("creat acount :select 1/visit acount: select 2 : ")
if start == 1:
    
elif start == 2:
    user_name =input("enter your user_name: ")
    password =input("enter your password")
    if user_name == "danu" and password =="1234":
        print("Login successful!")
        print("select the option you like")
        option=input("/Check Balance /Withdraw Money /Deposit Money /Exit :")
        
        if option == "Check Balance":
            print(balance)
    #==================================================
        elif option == "Withdraw Money":
            amount_1=int(input("enter your withdraw amount: "))
            if amount_1 <= balance :
                balance = balance-amount_1
                print("it is your new balance : ",balance)
                print("it is your withdraw amoount : ",amount_1)

            else:
                print("chek your withdraw amount!, it is greater than your balance")
    #==================================================

        elif   option == "Deposit Money":
            amount_2 = int(input("enter your deposit amount : "))
            if amount_2 > 0 :
                balance = balance + amount_2
                print("it is your new balance : " ,balance)
                print("it is your Deposit amoount : ",amount_2)
                
            
            else:
                print("chek your Deposit amount!, it is lower than 0 ")
    #=====================================================
        elif option == "exit":
            pass

else:
    print("select the crect option!")