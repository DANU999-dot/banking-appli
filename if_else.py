a = int(input("enter your marks:"))
if a>=75:
    print("result=A")
elif a>=65:
    print("result=B")
elif a>=55:
    print("result=C")
elif a>=35:
    print("result=S")
elif a>=0:
    print("result=F")
'''def id_make():
    account_num=1000
    count=0

    try:
        with open ("accounts.txt", "a") as file:
            for i in file:
                count+=1

    except FileNotFoundError:
        pass
    return str(account_num + count)'''
