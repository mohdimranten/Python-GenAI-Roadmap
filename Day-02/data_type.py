x = 5
print(type(x))

#write a program to Add two given number 

a = float(input("Enter First Number :"))
b = float(input("Enter Second Number :"))
c = a + b
print("Sum of two number is :",c)

#Write a program to Average two number

a = int(input("Enter the first value :"))
b = int(input("Enter the second value :"))

c = (a + b)/2
print("Average vlaue is :",c)

#write a programn to Convert temprature

c = float(input("Enter temprature in celsius :"))
f = ((c * 9) / 5) + 32
print("Temperature in Fahrenheit:",f)


print("Choose Temprature Type")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choise = int(input("Enter your choise (1 or 2 or 3 or 4) :"))

if(choise == 1):
    c = float(input("Enter temprature in celsius :"))
    f = ((c * 9) / 5) + 32
    print("Temprature in Fahrenheit :",f)

elif(choise == 2):
    f= float(input("Enter temprature in Fahrenheit :"))
    c = ((f - 32) * 5) / 9
    print("Temprature in Celsius :",c)

elif(choise == 3):
    c = float(input("Enter Temprature in Celsius :"))
    k = c + 273.15
    print("Temprature in Kelvin :", k)

elif(choise == 4):        
    k = float(input("Enter Temprature in Kelvin :"))
    c = k - 273.15
    print("Temprature in Celsius :",c)
else:
    print("Invalid Input")


# Write a program to swap two number

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))

# logic 1 
c = a
a = b
b = c

#logic 2

a, b = b, a

print("After swap the value of a is :",a)
print("After swap the value of b is :",b)



