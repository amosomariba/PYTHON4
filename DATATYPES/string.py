# String
first_name = "Amos"
last_name = "Omariba"

print(f"My name is {first_name} {last_name}.")


# Double string
s = """How are you?"""

print(s)

# Accessing characters in python string

name = "amosonsongoomariba"

name1 = "amos onsongo omariba"

print(name[2])  # Accessing using positive indexing
print(name[-4])  #  Accessing using negative indexing
print(name1.split())  # Split words separately
print(name1.capitalize())  # Capitalize the first letter
print(len(name1))  # Count letters
print(name1.upper())  # Make all letters into uppercase

# Slicing string
print(name[1:4])  # Retrieves characters from index 1 to 3
print(name[:3])  # Retrieves characters from index 0 to 2
print(name[3:])  # Starts to print from index 3
print(name[::-1])  # Reverse a string

# Delete a string
name2 = "amosonsongoomariba"

del name2 # Delete the string