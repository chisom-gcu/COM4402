# Simple Greeting
print("What is your name?")
name = input()
print("Hello", name)

# Name and Age Structure
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello", name + ", you are", age, "years old.")

# Age Next Year (Type Conversion)
name = input("Enter your name: ")
age = int(input("Enter your age: "))

age_next_year = age + 1
print("Hello", name, "next year you will be", age_next_year)

# Simple Two-Number Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum_value = a + b
product = a * b

print("Sum is", sum_value)
print("Product is", product)

# Product Cost Calculator
product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total_cost = price * quantity

print("You bought", quantity, "of", product_name)
print("Total cost is", total_cost)

# User Profile Program
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))
age_plus_one = age + 1
print("Hello", name)
print("Next year you will be", age_plus_one)
print("Your height is", height, "metres")

# Confusion Bug
age = int(input("Enter age: "))
age_next_year = age + 1
print("Next year you will be", age_next_year)

