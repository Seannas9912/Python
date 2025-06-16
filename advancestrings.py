#Advance concepts of strings in Python

message1 = 'Hello, World!'

print(message1[0])  # Accessing the first character

print(message1[7:12])  # Slicing to get 'World'

print(message1[7:])  # Slicing to get 'World!'

print(message1[-1])  # Accessing the last character

print(message1[-6:])  # Slicing to get 'World!'

print(message1.upper())  # Converting to uppercase

print(message1.lower())  # Converting to lowercase

print(message1.replace('World', 'Python'))  # Replacing 'World' with 'Python'

print(message1.split(','))  # Splitting the string into a list at the comma

print(message1.find('World'))  # Finding the index of 'World'

print(message1.startswith('Hello'))  # Checking if the string starts with 'Hello'

print(message1.endswith('!'))  # Checking if the string ends with '!'

print(len(message1))  # Getting the length of the string including spaces and punctuation

print(message1.strip())  # Stripping whitespace from both ends (not applicable here, but useful)