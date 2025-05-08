
'''i=1
while i <=3:
    a= input("user_name: ")
    b= input("password: ")
    if a == "danu" and b == "1234":
        print("Login successful!")
        break
    else:
        print("Too many failed attempts. Exiting program") 
        i=i+1
print("attempts no ",i)
'''
'''
i=0
while i<=10 and i%2==0:
    print(i)
    i=i+1
else:
    print("")'''
print("======(❁´◡`❁) Welcome to Banking (❁´◡`❁)======")
print("Create account: select 1 :")
print("Login account: select 2:")
start = input(":")

import random

# ========================= create account ============================
def create_account():
    account_num = str(random.randint(1, 100))

    balance = int(input("Enter your balance: "))
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    with open("accounts.txt", "a") as file:
        file.write(f"{account_num},{balance}\n")

    with open("password.txt", "a") as file:
        file.write(f"{account_num},{password}\n")

    with open("user_name.txt", "a") as file:
        file.write(f"{account_num},{name}\n")

    print(f"Account number is {account_num}. Your account was saved successfully! 😎")


# ========================= load password =============================
def load_password():
    passwords = {}
    try:
        with open("password.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    account_num, password = parts
                    passwords[account_num] = password
                else:
                    print("Skipping malformed line:", line.strip())
    except FileNotFoundError:
        print("Password file not found!")
    return passwords


# ========================= load user_name ============================
def load_user_name():
    user_name = {}
    try:
        with open("user_name.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    account_num, name = parts
                    user_name[account_num] = {"user_name": name, "balance": 0}
                else:
                    print("Skipping malformed line:", line.strip())
    except FileNotFoundError:
        print("user_name file not found!")
    return user_name


# ========================= load account balances =====================
def load_account_balances():
    balances = {}
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    account_num, balance = parts
                    balances[account_num] = int(balance)
                else:
                    print("Skipping malformed line in accounts:", line.strip())
    except FileNotFoundError:
        print("accounts.txt not found!")
    return balances


# ========================= save account updates ======================
def save_new_updates(accounts):
    with open("accounts.txt", "w") as file:
        for acc_num, data in accounts.items():
            file.write(f"{acc_num},{data['balance']}\n")


# ========================= withdraw ==================================
def withdraw(accounts, user_name):
    amount = int(input("Enter your withdraw amount: "))
    if amount <= accounts[user_name]["balance"]:
        accounts[user_name]["balance"] -= amount
        print("Transaction successful!")
        print("Your new balance is 🤑:", accounts[user_name]["balance"])
        save_new_updates(accounts)

        with open("history.txt", "a") as file:
            file.write(f"withdraw,{user_name},{accounts[user_name]['balance']}\n")
    else:
        print("Please check the amount. 🤦‍♂️")


# ========================= deposit ===================================
def deposit(accounts, user_name):
    amount = int(input("Enter your deposit amount: "))
    if amount > 0:
        accounts[user_name]["balance"] += amount
        print("Deposit successful!")
        print("Your new balance is 💸:", accounts[user_name]["balance"])
        save_new_updates(accounts)

        with open("history.txt", "a") as file:
            file.write(f"deposit,{user_name},{accounts[user_name]['balance']}\n")
    else:
        print("Invalid deposit amount! 😢")


# ========================= app logic =================================
if start == "1":
    create_account()

elif start == "2":
    accounts = load_user_name()
    passwords = load_password()
    balances = load_account_balances()

    print("(((φ(◎ロ◎;)φ)))")
    user_name = input("Enter your account number: ")
    password = input("Enter your password: ")

    if user_name in accounts and passwords.get(user_name) == password:
        # update balance from file
        if user_name in balances:
            accounts[user_name]["balance"] = balances[user_name]
        else:
            accounts[user_name]["balance"] = 0

        print("Login successful! 😎")
        while True:
            print("\n=============== Select an option ======================")
            print("Check Balance 😊 (c)")
            print("Withdraw Money 🤑 (w)")
            print("Deposit Money 💸 (d)")
            print("Exit 👋 (e): ")
            option = input(":")

            if option == "c":
                print("Your balance is 😊:", accounts[user_name]["balance"])
            elif option == "w":
                withdraw(accounts, user_name)
            elif option == "d":
                deposit(accounts, user_name)
            elif option == "e":
                print("Thank you for using banking! 👋")
                break
            else:
                print("Invalid option. Please try again 😢.")
    else:
        print("Invalid account number or password! 🤬")

else:
    print("Please select a correct option! 🙄")
