# Holton College Digital Quiz System.
print("Welcome to the Holton College Quiz!")
print("Please answer with the number (1, 2, 3, or 4).\n")

# Question Bank (List of Questions)
question_bank = [
    "What can a motherboard be known as?",
    "Which component is known as the 'brain' and fits  into a socket  on the motherboard?",
    "What does RAM stand for?",
    "Which part of the motherboard keeps the date and time, when the power is off?",
    "What do we call the 'roads' that data travels on across the motherboards?"
]

# Options (List of lists)
options = [
    ["The computer's brain","The central hub connecting all the parts", "A small portable storage stick", "The screen you look at"],
    ["RAM", "Hard Drive", "CPU", "Power Supply"],
    ["Real Apple Music", "Read All Messages", "Random Access Memory", "Run Another Memory"],
    ["CPU", "CMOS Battery", "Cooling Fan", "USB Port"],
    ["Trains", "Buses", "Cables", "Wi-Fi"]
]

# Answer key (List of Correct Answers)
answer_key = [2,3,3,2,2]

# Initialisation

score = 0

# Quiz Execution

for index in range(len(question_bank)):

    print(f"Question {index +1}: {question_bank[index]}")

    #Display options for the current question
    for option_number in range(4):
        print(f"{option_number + 1}. {options[index][option_number]}")


    # Get user input
    user_answer = input ("Your answer: ")

    #Validation and Scoring
    if user_answer.isdigit():
        user_answer = int(user_answer)

        if user_answer == answer_key[index]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")
    else:
        print("Invalid input. Question marked incorrect.\n")

# Result Display
print("Quiz Complete!")
print(f"You scored {score} out of {len(question_bank)} correct.")
print("Thank you for playing!")

