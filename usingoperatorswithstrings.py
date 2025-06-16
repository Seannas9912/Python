#Operators with Strings

str1 = "Hello"
str2 = "World"

print("Concatenation:", str1 + " " + str2)  # Output: Hello World
print("Repetition:", str1 * 3)  # Output: HelloHelloHello
print("Length of str1:", len(str1))  # Output: 5
print("Length of str2:", len(str2))  # Output: 5
print("Length of concatenated string:", len(str1 + " " + str2))  # Output: 11
print("Uppercase str1:", str1.upper())  # Output: HELLO
print("Lowercase str2:", str2.lower())  # Output: world
print("First character of str1:", str1[0])  # Output: H
print("Last character of str2:", str2[-1])  # Output: d
print("Substring of str1 (1 to 3):", str1[1:4])  # Output: ell
print("Is 'Hello' in str1?", "Hello" in str1)  # Output: True
print("Is 'World' in str1?", "World" in str1)  # Output: False
print("Is 'Hello' not in str2?", "Hello" not in str2)  # Output: True
print("Formatted string:", f"{str1} {str2}")  # Output: Hello World
print("Formatted string with length:", f"{str1} {str2} - Length: {len(str1 + ' ' + str2)}")  # Output: Hello World - Length: 11