#Operators Data Types

#Arithmetic Operators
# These operators are used to perform mathematical operations on numeric values.
#Addition(+)
#Subtraction(-)
#Multiplication(*)
#Division(/)
#Floor Division(//)
#Modulus(%)
#Exponentiation(**)

x = 10
y = 2

print("Addition:", x + y)          # Output: 12
print("Subtraction:", x - y)       # Output: 8
print("Multiplication:", x * y)     # Output: 20
print("Division:", x / y)           # Output: 5.0
print("Floor Division:", x // y)    # Output: 5
print("Modulus:", x % y)            # Output: 0 because it counts the remainder after division
print("Modulus:", x % 3)            # Output: 1 because 10 divided by 3 leaves a remainder of 1
print("Exponentiation:", x ** y)    # Output: 100

#assignment operators
# These operators are used to assign values to variables.

g = 10
g += 2  # Equivalent to g = g + 2
a = 10
a -= 2  # Equivalent to a = a - 2
b = 10
b *= 2  # Equivalent to b = b * 2
c = 10
c /= 2  # Equivalent to c = c / 2
d = 10
d //= 2  # Equivalent to d = d // 2
e = 10
e %= 2  # Equivalent to e = e % 2
f = 10
f **= 2  # Equivalent to f = f ** 2
print("Addition Assignment:", g)  # Output: 12
print("Subtraction Assignment:", a)  # Output: 8
print("Multiplication Assignment:", b)  # Output: 20
print("Division Assignment:", c)  # Output: 5.0
print("Floor Division Assignment:", d)  # Output: 5
print("Modulus Assignment:", e)  # Output: 0
print("Exponentiation Assignment:", f)  # Output: 100