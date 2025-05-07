print("======(❁´◡`❁) Welcome to Banking (❁´◡`❁)======")
start = input("Create account: select 1 / Visit account: select 2 : ")

# ========================= create account ============================
def create_account():
    account_num = 1009  
    balance = int(input("Enter your balance amount: "))
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    with open("accounts.txt", "a") as file:
        file.write(f"{account_num},{name},{password},{balance}\n")

    print("Account created and saved successfully!")

# ========================= load account ============================================
def load_accounts():
    accounts = {}
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    account_num, name, password, balance = parts
                    accounts[name] = {"password": password, "balance": int(balance)}
                else:
                    print("Skipping malformed line:", line.strip())
    except :
        print("Accounts file not found!")
    return accounts


# ========================= withdraw =================================
def withdraw(accounts, user_name):
    amount = int(input("Enter your withdraw amount: "))

    if amount <= accounts[user_name]["balance"]:
        accounts[user_name]["balance"] -= amount
        print("Transaction successful!")
        print("Your new balance is:", accounts[user_name]["balance"])
        save_accounts(accounts)
    else:
        print("Insufficient balance! Please check the amount.")

# ========================= deposit =================================
def deposit(accounts, user_name):
    amount = int(input("Enter your deposit amount: "))

    if amount > 0:
        accounts[user_name]["balance"] += amount
        print("Deposit successful!")
        print("Your new balance is:", accounts[user_name]["balance"])
        save_accounts(accounts)
    else:
        print("Invalid deposit amount!")

# ========================= save account ============================
def save_accounts(accounts):
    with open("accounts.txt", "w") as file:
        for name, data in accounts.items():
            file.write(f"1009,{name},{data['password']},{data['balance']}\n")

# ========================= code for app ===============================
if start == "1":
    create_account()
elif start == "2":
    accounts = load_accounts()
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    if user_name in accounts and accounts[user_name]["password"] == password:
        print("Login successful!")
        while True:
            option = input("\nSelect an option:\n"
                           "Check Balance (c)\n"
                           "Withdraw Money (w)\n"
                           "Deposit Money (d)\n"
                           "Exit (e): ").lower()
            
            if option == "c":
                print("Your balance is:", accounts[user_name]["balance"])
            elif option == "w":
                withdraw(accounts, user_name)
            elif option == "d":
                deposit(accounts, user_name)
            elif option == "e":
                print("Thank you for use banking!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Invalid username or password!")
else:
    print("Please select a correct option!")
