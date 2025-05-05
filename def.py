
# ge
'''
a= int(input("enter num 1: "))
b= int(input("enter num 2: "))

def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def mul(x,y):
    print(x*y)

def div(x,y):
    print(x/y)

add(a,b)  
sub(a,b)
mul(a,b)
div(a,b)'''
balance=100000
D_amount=int(input("enter the d_amount:"))
# create deposit system
def deposit(balance,D_amount):
    
    if  D_amount <= 0:
        print("add amount greater than 0.")
    else:
        balance += D_amount
        print("deposited is", D_amount," New balance is", balance)

# create withdraw system
def withdraw(balance, W_amount):
    if W_amount >0 and W_amount<= balance :
        balance -= W_amount
        print("you aer withdrow",W_amount,"now account balance is", balance)
    else:
        print("your amount is not velide")


a=input("what you want?deposit/withdraw/show balance/exit:")
if a=="deposit":
   deposit()
elif a== "exit":
    print("thank you for your try")
elif a== "withdraw":
   withdraw()
elif a=="show balance":
    print(balance)

'''
# Initial balance
balance = 100000

# Deposit function
def deposit(balance, D_amount):
    if D_amount <= 0:
        print("Add amount greater than 0.")
    else:
        balance += D_amount
        print("Deposited:", D_amount, "New balance is:", balance)
    return balance

# Withdraw function
def withdraw(balance, W_amount):
    if W_amount > 0 and W_amount <= balance:
        balance -= W_amount
        print("You have withdrawn:", W_amount, "New balance is:", balance)
    else:
        print("Invalid amount. Either negative or exceeds balance.")
    return balance

# Main loop
while True:
    choice = input("What do you want? (deposit/withdraw/show balance/exit): ").lower()
    
    if choice == "deposit":
        D_amount = int(input("Enter the amount to deposit: "))
        balance = deposit(balance, D_amount)
    
    elif choice == "withdraw":
        W_amount = int(input("Enter the amount to withdraw: "))
        balance = withdraw(balance, W_amount)
    
    elif choice == "show balance":
        print("Current balance is:", balance)
    
    elif choice == "exit":
        print("Thank you for using the bank system.")
        break
    
    else:
        print("Invalid input. Please try again.")
'''