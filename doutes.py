#file=open("sampil.txt","r")
#print(file.read())
list = []
balance=500000
print("======(❁´◡`❁)wellcome to banking(❁´◡`❁)======")
start =input("creat acount :select 1/visit acount: select 2 : ")
account_num=000
#============================================================
def create_account():
    account_num = input("Enter your account number: ")
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    with open("accounts.txt", "a") as file:
        file.write(f"{account_num},{name},{password}\n")
    
    print("Account created and saved successfully!")


#dictionary============================================
'''
accounts = {
    "danu": {"password": "1234", "balance": 500000},
    "raj": {"password": "5678", "balance": 750000}
}'''
#=====================================================
#function=============================================
load_accounts():
accounts = {}
try:
    with open("accounts.txt", "r") as file:
        for line in file:
            account_num, name, password, balance = line.strip().split(",")
            accounts[name] = {"password": password, "balance": int(balance)}
except FileNotFoundError:
    print("Accounts file not found!")
return accounts

#withdraw function===============================================
'''def withdraw():
    accounts = load_accounts()
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    if user_name in accounts and accounts[user_name]["password"] == password:
        print("Login successful!")
        amount = int(input("Enter your withdraw amount: "))

        if amount <= accounts[user_name]["balance"]:
            accounts[user_name]["balance"] -= amount
            print("Transaction successful!")
            print("Your new balance is: ", accounts[user_name]["balance"])
            
            # Updated data file-ல் சேமிக்க
            with open("accounts.txt", "w") as file:
                for name, data in accounts.items():
                    file.write(f"{data['balance']},{name},{data['password']},{data['balance']}\n")
        else:
            print("Insufficient balance! Please check the amount.")
    else:
        print("Invalid username or password!")'''

#deposit funtion======================================
def deposit():
        accounts = load_accounts()
        amount = int(input("Enter your  deposit amount: "))

        if amount >0:
            accounts[user_name]["balance"] += amount
            print(" deposit successful!")
            print("Your new balance is: ", accounts[user_name]["balance"])
            
            # Updated data file-ல் சேமிக்க
            with open("accounts.txt", "w") as file:
                for name, data in accounts.items():
                    file.write(f"{data['balance']},{name},{data['password']},{data['balance']}\n")
        else:
            print("Insufficient amount! Please check the amount.")
#=====================================================

def withdraw():
        amount = int(input("Enter your withdraw amount: "))
        
        if amount <= accounts[user_name]["balance"]:
            accounts[user_name]["balance"] -= amount
            print("Transaction successful!")
            print("Your new balance is: ", accounts[user_name]["balance"])
        else:
            print("Insufficient balance! Please check the amount.")
    


# make function=== ====================================================================
def withdraw_1(): 
    global balance
    amount_1=int(input("enter your withdraw amount: "))
    if amount_1 <= balance :
        balance = balance-amount_1
        list.append()
        print("it is your new balance : ",balance)
        print("it is your withdraw amoount : ",amount_1)
    else:
        print("chek your withdraw amount!, it is greater than your balance")

def Deposit_1():
    global balance
    amount_2 = int(input("enter your deposit amount : "))
    if amount_2 > 0 :
        balance = balance + amount_2
        print("it is your new balance : " ,balance)
        print("it is your Deposit amoount : ",amount_2) 
    else:
        print("chek your Deposit amount!, it is lower than 0 ")
# start banking==========================================================================

i=0
if start == "1":
    create_account()
        
    
    
elif start == "2":
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    if user_name in accounts and accounts[user_name]["password"] == password:
        print("Login successful!")
        print("select the option you like")
        while True:
            option=input("/Check Balance press(c) /Withdraw Money press(w) "
            "/Deposit Money press(d) /Exit press(e) :")
            if option == "c":
                print(balance)
                
#withdraw =======================================================
            elif option == "w":
                withdraw()

#Deposit =========================================================
            elif   option == "d":
                Deposit()
            
#exit ============================================================
            elif option == "e":
                print("thank you for your try!")
    else:
        print("Invalid username or password!")
else:
    print("select the crect option!")
