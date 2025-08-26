#Loops and control statements


#For loop example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue # Skip the iteration for "banana"
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "banana":
        break # Stop the loop when "banana" is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "banana":
        pass # Do nothing for "banana":
    print(fruit)
    
print()

# While loop example
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    if( countdown == 3):
        continue # Skip the iteration when countdown is 3
    
print()

while countdown > 0:
    if countdown == 3:
        break # Stop the loop when countdown is 3
    print(countdown)
    countdown -= 1
    
print()
while countdown > 0:
    if countdown == 3:
        pass # Do nothing for 3
    print(countdown)
    countdown -= 1