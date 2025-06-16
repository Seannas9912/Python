#loops
#two types of loops: for and while
#for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number) #single value per iteration
#while loop
#while loop to print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1 #increment the count
    
#Loop control statements
#break statement
for number in range(1, 11):
    if number == 6:
        break  # exit the loop when number is 6
    print(number)
    
#continue statement
for number in range(1, 11):
    if number % 2 == 0:
        continue  # skip even numbers
    print(number)
    
#pass statement
for number in range(1, 11):
    if number == 5:
        pass  # do nothing for number 5
    print(number)
    
#Nested loops
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i: {i}, j: {j}")
        
#Looping through a string
for char in "hello":
    print(char)
    
#Looping through a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
    
#Looping through a set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
    
#Using range() function
for i in range(5):  # prints numbers from 0 to 4
    print(i)
    
#Using range() with start, stop, and step
for i in range(1, 10, 2):  # prints odd numbers from 1 to 9
    print(i)
    
#Using enumerate() to get index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
    
#Using zip() to loop through multiple lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, letter in zip(list1, list2):
    print(f"Number: {num}, Letter: {letter}")
    
#Using list comprehension for looping
squares = [x**2 for x in range(10)]  # creates a list of squares from 0 to 9
print(squares)

#Using a loop with a condition
for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # increment the count
    if count == 3:
        print("Count reached 3, breaking the loop.")
        break