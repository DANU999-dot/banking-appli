#get input================================================================
a= input("user_name: ")
b= input("password: ")

balance=50000

if a == "danu" and b == "1234":
    print("Login successful!")
    print("select the option you like")
    option=input("Check Balance /Withdraw Money /Deposit Money /Exit :")
#Check Balance =============================================================        
    if option == "Check Balance":
        print(balance)
#Withdraw Money ============================================================
    elif option == "Withdraw Money":
        amount=int(input("enter your withdraw amount: "))
        balance=balance-amount
        print("your corenly balance is",balance,"LKR")
        print("you are withdraw ",amount,"LKR")
#Deposit Money==============================================================
    elif option == "Deposit Money":
        amount_1=int(input("enter your Deposit amount: "))
        balance=balance+amount_1
        print("your corenly balance is",balance,"LKR")
        print("you are withdraw ",amount_1,"LKR")
#exit=======================================================================
    elif option == "exit":
        print("thank you for your try ")

#===========================================================================
else:
    print("Too many failed attempts. Exiting program")