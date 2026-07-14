#Login Sysytem 
usr = "admin"
psw = "123456"

username = input("Enter Username :")
password = input("Enter Password :")


if(username==usr and password==psw):
    print("Login Successfully")
else:
    print("Invalid Login!")   



#Login Sysytem with 3 attempt     

usr  = "admin"
psw = "123456"
attempt = 3

while attempt > 0:
    username = input("Enter Username :")
    password = input("Enter Password :")

    if(username==usr and password==psw):
        print("Login Successfully")
    else:
        attempt -= 1
        print("username or password are incorrect")
        print("Remaining attempt is :",attempt)


if(attempt == 0):
    print("Account Locked!Contact to Administration")     


