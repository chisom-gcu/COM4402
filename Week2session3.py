score = int(input("Enter score: "))

if score >= 40:
    print("Pass")
else:
    print("Fail")

score = int(input("Enter score (0–100): "))

if score >= 70:
    grade = "Distinction"
elif score >= 40:
    grade = "Pass"
else:
    grade = "Fail"

print("Your grade is:", grade)

score = int(input("Enter score (0–100): "))
if score >= 40:
    if score >= 70:
        print("Pass with merit")
    else:
        print("Pass")
else:
    print("Fail")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "secret":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Unknown username")



# # Cinema Ticket Category
age = int(input("Enter your age: "))

if age < 5:
    print("Free entry")
elif age <= 17:
    print("Child ticket")
elif age <= 64:
    print("Adult ticket")
else:
    print("Senior ticket")

# Library Fine Calculator
days_late = int(input("Days Late: "))

if days_late == 0:
    print("No fine")
elif days_late <= 5:
    print("Fine = £1")
elif days_late <=10:
    print("Fine = £5")
else:
    print("Fine = £10 and membership review")

# # Exam Borderline Check (Nested)
score = int(input("Enter Score (0-100): "))

if score >= 40:
    if 38 <= score <= 42:
        print("Borderline pass, consider review.")
    else:
        print("Clear pass.")

else:
    print("Fail.")

# # Discount Eligibility
is_student = input("Are you a student? (yes/no): ")
age = int(input("Enter your age: "))

if is_student == "yes" or age < 18:
        print("Discount applied")
else:
        print("No discount")

# # Traffic Light Action
colour = input("Enter a colour (red, amber, or green): ")
colour = colour.lower()

if colour == "red":
    print("Stop")
elif colour == "amber":
    print("Get ready")
elif colour == "green":
    print("Go")
else:
    print("Invalid colour")

# # Multiple of 3,5 or Both
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("No match")

# # Meal Recommendation
time_day = input("Enter time of day (morning, afternoon, evening): ")
is_hungry =  input("Are you hungry (yes/no): ")

if is_hungry == "no":
    print("Have some water and rest.")
if is_hungry == "yes":
    if time_day == "morning":
        print("Have breakfast")
    elif time_day == "afternoon":
        print("Have lunch")
    elif time_day == "evening":
        print("Have dinner")
    else:
        print("snack time")

# Module Mark Status
coursework_mark = int(input("Enter coursework mark (0-100): "))
exam_mark = int(input("Enter exam mark (0-100): "))

average = (coursework_mark + exam_mark)/2

if coursework_mark <35 or exam_mark < 35:
    print("Automatic fail (component below 35).")
elif average >= 40:
    print("Module passed.")
else:
    print("Module failed (average below 40).")

# Simple Two-Stage Verification
pin = int(input("Enter a 4-digit pin: "))

if pin == 1234:
    colour = input("What is your favourite colour?: ")
    if colour == "blue":
        print("Access granted.")
    else:
        print("Security answer incorrect.")
else:
    print("Wrong PIN.")

# Sport Suggestion by Weather and Mood
weather = input("Enter weather (sunny, rainy,cold): ")
mood = input("Enter mood (active, tired): ")

if weather == "sunny" and mood == "active":
    print("Go for a run.")
elif weather == "sunny" and mood == "tired":
    print("Relax in the park.")
elif weather == "rainy":
    print("Indoor workout.")
elif weather == "cold":
    print("Go to the gym.")
else:
    print("No suggestion available.")