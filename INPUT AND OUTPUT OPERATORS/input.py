name = input("Enter your name: ") #input function is used to take input from the user

try:
    age = int(input("Enter your age: "))
    print(f"Hello {name}, you are {age} years old") #f-string is used to format the string
except ValueError:
    print("Invalid input. Please enter a valid integer.") #if the input is not a valid integer, the program will print this message

#type function is used to check the type of the variable (typecasting)
print(type(name))
print(type(age))

# name=input("Enter your name: \n")
# age=input("Enter your age: \n")

# print(f"Hello {name}, you are {age} years old")

# name=input("Enter your name fullnames: ")

# print(name.split())

# print(name.upper())

# print(name.lower())

# print(name.strip())

# print(name.title())

# print(len(name))

# print(name.count("a"))

# print(name.find("a"))

# print(name.replace("a", "b")) 


