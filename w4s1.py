# #
# def greet(name):
#     print(f"Hello {name}!")
#
# greet("Aisha")
# greet("Bilal")
#
#
# #
# def add(a, b):
#     result = a + b
#     return result
#
# total = add(3, 4)
# print("Total is", total)

def add(numa, numb):
    print(f"sum -> {numa + numb}")


a = int(input("Enter A: "))
b = int(input("Enter B: "))

op = input("Enter +, -, *, or /: ")

if op == "+":
    add(a, b)
elif op == "-":
    sum(a, b)

# Fix the Greeting
def greet():
    message = "Hello from the function"

greet()
print(message)

# Global Variable
message = "Hello from outside"

def greet():
    print(message)

greet()
print(message)
#
message = "Global message"

def greet():
    message = "Local message"
    print("Inside:", message)

greet()
print("Outside:", message)
#
def greet(name):
    message = f"Hello {name}"
    print(message)

greet("Aisha")


# Local vs Global Guess
count = 0

def add_one(count ):
    count = count + 1
    print("Inside:", count)
    return count

count = add_one(count)
print("Outside:", count)

# Complete the function
def area_of_rectangle(width, height):
     area = width * height
     return area

 w = float(input("Enter width: "))
 h = float(input("Enter height: "))

result = area_of_rectangle(w, h)
print("Area is ", result)

# Parameter vs Global
rate = 0.2

def calculate_tax(amount):
    return amount * rate

price = float(input("Enter amount: "))
tax = calculate_tax(price)
print("Tax is", tax)
#
def calculate_tax(amount, rate):
    return amount * rate

price = float(input("Enter amount: "))
rate = 0.2

tax = calculate_tax(price, rate)
print("Tax is", tax)

# Bug Hunt: Discount Function
def apply_discount(price):
    if price > 100:
        discount = 10
    else:
        discount = 0
    return price - discount

p = float(input("Enter price: "))
result = apply_discount(p)
print("Final price:", result)

# ATM Helper Functions
def show_menu():
    print("1. Deposit")
    print("2. Withdraw")
    print("0. Exit")
    choice = input("Enter choice: ")
    return choice

def deposit(balance):
    amount = float(input("Amount to deposit: "))
    if amount > 0:
        balance = balance + amount
    else:
        print("Invalid deposit amount")
    return balance

def withdraw(balance):
    amount = float(input("Amount to withdraw: "))
    if amount > 0 and amount <= balance:
        balance = balance + amount
    else:
        print("Invalid deposit amount")
    return balance
#

# Scope
total = 0

def add_mark(mark):
    total = total + mark
    return total

mark1 = int(input("Enter mark 1: "))
total = add_mark(mark1)

mark2 = int(input("Enter mark 2: "))
total = add_mark(mark2)

print("Total:", total)