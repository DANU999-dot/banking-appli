print("======(❁´◡`❁) Welcome to Banking (❁´◡`❁)======")
print("Create account: select 1 :")
print("login account: select 2:")\
#============================creat history============================================

def history():
    try:
        with open("history.txt", "r") as file:
            print("Transaction History:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("History file not found!")


# ========================= create account ===================================================
import random

def create_account():
    account_num = random.randint(1,100) 
        
    balance = int(input("enter your balance: "))
    name = input("enter your name: ")
    password = input("enter your password: ")

    with open("accounts.txt", "a") as file:
        file.write(f"{account_num},{balance}\n")                                                                                                                                                                           

    with open("password.txt","a") as file:
        file.write(f"{account_num},{password}\n")

    with open ("user_name.txt","a") as file:
        file.write(f"{name},{password}\n")

    print(f"acount_num is {account_num} your account saved succsesfully!😎")


#=========================load password========================================

def load_accounts():
    accounts = {}
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
               
                if len(parts) == 4:
                    account_num, name, password, balance = parts
                    accounts[name] = {"account_num": account_num, "password":password, "balance": int(balance)}
                else:
                    print("Skipping malformed line:", line.strip())
    
    except FileNotFoundError:
        print("Accounts file not found!")
    
    return accounts
'''def load_password():
    passwords = {}
    try:
        with open("password.txt", "r") as file:
            for lines in file:
                parts = lines.strip().split(",")
                if len(parts) == 2:
                    account_num,password = parts
                    passwords[password] = password
                else:
                    print("Skipping malformed line:", lines.strip())
    except FileNotFoundError:
        print("Password file not found!")
    return passwords
#============================lode user_name =========================================
def load_user_name():
    user_name = {}
    try:
        with open("user_name.txt", "r") as file:
            for line in file:
                part = line.strip().split(",")
               
                if len(part) == 1:
                    name = part
                    user_name[name] = {"user_name": name}
               
                else:
                    print("Skipping malformed line:", line.strip())
    
    except :
        print("user_name file not found!")
    
    return user_name'''
# ========================= save account ====================================
def save_new_updates(accounts,account_num):
    with open("accounts.txt", "w") as file:
        for name, data in accounts.items():
            file.write(f"{account_num},{data['balance']}\n")

# ========================= withdraw =============================================
def withdraw(accounts, user_name,account_num, password):
    try:
        amount = int(input("Enter your withdrawal amount: "))
        if amount <= accounts[user_name]["balance"]:
            accounts[user_name]["balance"] -= amount
            print("Transaction successful!")
            print("Your new balance is🤑:", accounts[user_name]["balance"])
        
            save_new_updates(accounts, account_num)
    
            with open("history.txt", "a") as file:
                file.write(f"withdraw,{user_name},{password},{accounts[user_name]['balance']}\n")
        else:
            print(" Please check the amount.🤦‍♂️")
    except ValueError:
        print("Invalid input! Please enter a valid number.😢")
# ========================= deposit ==============================================================
def deposit(accounts, user_name, account_num):
    try:
        amount = int(input("Enter your deposit amount: "))

        if amount > 0:
            accounts[user_name]["balance"] += amount
            print("Deposit successful!")
            print("Your new balance is💸:", accounts[user_name]["balance"])

            save_new_updates(accounts, account_num)

            with open("history.txt", "a") as file:
                file.write(f"deposit,{user_name},{accounts[user_name]['balance']}\n")
        else:
            print("Invalid deposit amount!😢")
    except ValueError:
        print("Invalid input! Please enter a valid number.😢")
# ========================= code for app ==============================================
start = input(":")
if start == "1":
   create_account()



elif start == "2":
    import getpass
    accounts = load_accounts()
    print("(((φ(◎ロ◎;)φ)))")
    user_name = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

  #  if True :
    if user_name in accounts and accounts[user_name]["password"] == password:
   # if user_name in accounts and word.get(password) == password:

        print("Login successful!😎")
        while True:
            print("===============Select an option======================\n"
                           "Check Balance😊 (c)\n"
                           "\n"
                           "Withdraw Money 🤑(w)\n"
                           "\n"
                           "Deposit Money💸 (d)\n"
                           "\n"
                           "transaction history (t)"
                           "\n"
                           "Exit 👋(e): ")
            option=input(":")
            
            if option == "c":
                print("Your balance is😊:", accounts[user_name]["balance"])
            
            elif option == "w":
                withdraw(accounts, user_name, password)
            
            elif option == "d":
                deposit('accounts', 'user_name','account_num')
            elif option == "t":
                history()
                 
            elif option == "e":
                print("Thank you for use banking!👋")
                break
            
            else:
                print("Invalid option. Please try again😢.")
                break
    
    else:
        print("Invalid username or password!🤬")

else:
    print("Please select a correct option!🙄")

#456#
