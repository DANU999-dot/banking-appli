
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

i=0
while i<=10 and i%2==0:
    print(i)
    i=i+1
else:
    print("")