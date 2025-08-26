fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Accessing the first element

fruits[1] = "blueberry"  # Modifying the second element
print(fruits)

fruits.append("orange")  # Adding a new element to the end
print(fruits)

fruits.insert(1, "kiwi")  # Inserting an element at a specific position
print(fruits)

fruits.sort()  # Sorting the list in ascending order
print(fruits)

fruits.sort(reverse=True)  # Sorting in descending order
print(fruits)

fruits.remove("blueberry")  # Removing an element
print(fruits)