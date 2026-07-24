# ----------------------------------------
# Holton College Motherboard Quiz
# ----------------------------------------

print("Welcome to the Holton College Quiz!")
print("Please answer with the number (1, 2, 3, or 4).\n")

# ----------------------------------------
# DATA STORAGE: List of dictionaries
# ----------------------------------------
questions = [
    {
        "question": "What is the best way to describe a motherboard?",
        "options": [
            "The computer's brain",
            "The central hub connecting all parts",
            "A small portable storage stick",
            "The screen you look at"
        ],
        "answer": 2
    },
    {
        "question": "Which component is known as the 'brain'?",
        "options": [
            "RAM",
            "Hard Drive",
            "CPU",
            "Power Supply"
        ],
        "answer": 3
    },
    {
        "question": "What does RAM stand for?",
        "options": [
            "Real Apple Music",
            "Read All Messages",
            "Random Access Memory",
            "Run Another Memory"
        ],
        "answer": 3
    },
    {
        "question": "Which part keeps the date and time when power is off?",
        "options": [
            "CPU",
            "CMOS Battery",
            "Cooling Fan",
            "USB Port"
        ],
        "answer": 2
    },
    {
        "question": "What do we call the 'roads' that data travels on?",
        "options": [
            "Trains",
            "Buses",
            "Cables",
            "Wi-Fi"
        ],
        "answer": 2
    }
]

# ----------------------------------------
# INITIALISATION
# ----------------------------------------
score = 0

# ----------------------------------------
# QUIZ EXECUTION
# ----------------------------------------
for i, question in enumerate(questions, start=1):
    print(f"Question {i}: {question['question']}")

    # Display the options
    for num, option in enumerate(question["options"], start=1):
        print(f"{num}. {option}")

    # Input with validation
    valid_input = False
    while not valid_input:
        user_answer = input("Your answer: ")
        try:
            user_answer = int(user_answer)
            if 1 <= user_answer <= 4:
                valid_input = True
            else:
                print("Invalid input. Enter a number between 1 and 4.\n")
        except ValueError:
            print("Error: Input must be a number (1-4).\n")

    # Check answer and update score
    if user_answer == question["answer"]:
        print("Correct!\n")
        score += 1
    else:
        correct_option = question["options"][question["answer"] - 1]
        print(f"Incorrect. The correct answer was {question['answer']}. {correct_option}\n")

# ----------------------------------------
# RESULTS DISPLAY
# ----------------------------------------
percentage = (score / len(questions)) * 100

print("Quiz Complete!")
print(f"You scored {score} out of {len(questions)} correct.")
print(f"Percentage: {percentage:.0f}%")
print("Thank you for playing!")