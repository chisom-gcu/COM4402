print("1. Say hello")
print("2. Say goodbye")
print("3. Say your name")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Hello!")
elif choice == 2:
    print("Goodbye!")
elif choice == 3:
    print("My name is Python.")
else:
    print("Invalid choice")


print("1. Say hello")
print("2. Say goodbye")
print("3. Say your name")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Hello!")
    case 2:
        print("Goodbye!")
    case 3:
        print("My name is Python.")
    case _:
        print("Invalid choice")