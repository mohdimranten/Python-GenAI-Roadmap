# Password Strength Checker

password = input("Enter a password :")

has_upper = False
has_lower = False
has_numeric = False
has_special =  False

special_chars = "!@#$%^&*()-_=+[]{};:,.<>?/"


for char in password:
    if(char.isupper()):
        has_upper = True
    elif(char.islower()):
        has_lower = True
    elif(char.isnumeric()):
        has_numeric = True
    elif char in special_chars:
        has_special = True

score = 0

if(len(password)>=8):
    score +=1
if(has_upper):
    score +=1
if(has_lower):
    score +=1
if(has_numeric):
    score +=1
if(has_special)      :
    score +=1

if(score<=2):
    print("Password Strength is Weak 🔴")
elif(score >2 and score <=4):
    print("Passowrd Strength is Medium 🟡")    
else:
    print("Password Strength is Strong 🟢")                       

