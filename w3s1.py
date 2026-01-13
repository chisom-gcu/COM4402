# file for week 3 session 1
students = ["Aisha", "Bilal", "Chen", "Dina"]

for name in students:
    print("Hello", name)

#
word = "Python"

for ch in word:
    print(ch)

#
word = input("Enter a word: ")
word = word.lower()
vowels = 0

for ch in word:
    if ch in "aeiou":
        vowels = vowels + 1

print("Number of vowels:", vowels)

#
numbers = [3, 4, 7, 10, 11]

for n in numbers:
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

#
n = int(input("How many marks? "))

total = 0

for i in range(n):
    mark = int(input(f"Enter mark {i+1}: "))
    total = total + mark

average = total / n
print("Total:", total)
print("Average:", average)

# Even numbers from 0 to 10
for n in range(0, 11, 2):
    print(n)

# Countdown from 5 to 1
for n in range(5, 0, -1):
    print(n)

start = int(input("Start from: "))

for n in range(start, 0, -1):
    print(n)

print("Go!")


# Repeat a Word
word = input("Enter a word: ")
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(f"{i}: {word}")

# Sum of First N Numbers
n = int(input("Enter an integer: "))

total = 0
for i in range(1, n + 1):
    total += 1

print("The sum is: ", total)

# Multiplication Table
x = int(input("Enter a number: "))

for i in range(1,11):
    print(i, "x", x, "=", i * x)

# Count characters
sentence = input("Enter a sentence: ")
count = 0
for char in sentence:
    if char != " ":
        count += 1

print ("Number of non-space characters:", count)

# Find Maximum Mark
count = int(input("How many marks will you enter? "))
max_mark = 0
for i in range (count):
    mark = int(input("Enter mark: "))
    if mark > max_mark:
        max_mark = mark

print("The highest mark:", max_mark)

# Filter Passing Marks
count = int(input("How many marks will you enter? "))
passed = 0
for i in range(count):
    mark = int(input("Enter mark:" ))
    if mark >= 40:
        print(mark)
        passed +=1

print("The number of students who passed:", passed)

# Reverse a String (Manual)
word = input("Enter a word: ")

reversed_word = ""
for char in word:
    reversed_word = char + reversed_word

print(" Reversed word:", reversed_word)

# Count Specific Letter in a List of Names
