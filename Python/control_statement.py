num=-6

if num>0:
    print("Positive")
elif num==0:
    print("Zero")
else:
    print("Negative")
    
print()
  
num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))

if num1>num2:
    print(num1, "is greater than", num2)
elif num1<num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)