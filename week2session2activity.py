# name = "Chisom"
# age = 18
# print(f"Hello {name}, you are {age} years old")

# # Receipt with Formatting 1
item_name = input("Enter  item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total_cost = price * quantity

print("You bought", quantity, "of", item_name)
print("Total cost is", total_cost)


# Receipt with Formatting 2
item_name = "Coffee"
price = 2.5
quantity = 3

total = price * quantity

print(f"You bought, {quantity}, of, {item_name} at {total} each. Total = {total}")

# Age Description
age = 18
print(f"You are {age} years old.")

#Tidy Name & Course
full_name = "Alice Smith"
course_name ="COM4402"

print(full_name.strip().title())
print(course_name.strip().upper())
print(f"Student: {full_name} {course_name}")











