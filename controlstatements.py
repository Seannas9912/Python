#Control Statements
# if statement
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5
# if-else statement
if x < 5:
    print("x is less than 5")
else:
    print("x is not less than 5")
# if-elif-else statement
if x < 5:
    print("x is less than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is greater than 5")
# Nested if statement
if x > 5:
    print("x is greater than 5")
    if x > 10:
        print("x is also greater than 10")
    else:
        print("x is not greater than 10")
# Ternary operator
y = 20
result = "y is greater than 10" if y > 10 else "y is not greater than 10"
print(result)  # Output: y is greater than 10
# Using logical operators
a = True
b = False
if a and b:
    print("Both a and b are True")
elif a or b:
    print("At least one of a or b is True")
else:
    print("Neither a nor b is True")
    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# if-else statement to compare two numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")