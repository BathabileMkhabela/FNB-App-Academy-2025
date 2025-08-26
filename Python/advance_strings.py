message=" Hello, World! "

print(len(message))
print(message[0])
print(message[1])
print(message[5])
print(message[-1])

#using String methods
print(message.lower()) #changes all  the letters to lower cases
print(message.strip()) #this strip away all the whitespaces
print(message.upper()) #changes all  the letters to upper cases
print(message.split(',')) #it split in to separate list
print(message.replace('Hello', 'Goodbye')) #it replaces the word Hello with Goodbye
print(message.find('World')) #it finds the index of the word World


