x = 3
y = 4

c = x + y
print(c)

# Assignment Operators

a = 4

# Ternary Operator
x = 6
X = "Weekend!" if x > 5 else "Working"

print(X)

#Mini calculator

print("----Simple Calculator-----")
a = float(input("Enter the first value :"))
b = float(input("Enter the second value :"))

print("\nChoose Operations-")
print("1. Addition")
print("2. Substraction")
print("3. Multification")
print("4. Dividation")

choose_value = int(input("Choose number 1 or 2 or 3 or 4 :"))

if(choose_value == 1):
    add = a+b
    print("Sum is :",add)
elif(choose_value == 2):
    sub = a-b
    print("Sub is :",sub)    
elif(choose_value == 3):
    mul = a*b
    print("Multification is :",mul) 
elif(choose_value == 4):
    div = a/b
    print("Dviision is :",div)
else:
    print("Invalid value")           