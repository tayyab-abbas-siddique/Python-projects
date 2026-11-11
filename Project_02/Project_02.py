# Introduction of problem
print("================================")
print("PYTHON QUIZ APPLICATION")
print("================================")
print("\nWelcome to the Quiz!")

# Initials
count = 0

# ----------------First question----------------
# Question
print("""
What is the capital of Pakistan?

A. Lahore
B. Multan
C. Islamabad
D. Karachi""")

# Option
first_q = input("Your answer: ")
first_q = first_q.upper()

# Checking
if first_q == "C":
    print("Correct Answer!")
    count += 1
else:
    print("Incorrect Answer! The correct answer was Islamabad.")

# ----------------Second question----------------
# Question
print("""
Which language is used for web structure?

A. Python
B. Java
C. HTML
D. C""")

# Option
second_q = input("Your answer: ")
second_q = second_q.upper()

# Checking
if second_q == "C":
    print("Correct Answer!")
    count += 1
else:
    print("Incorrect Answer! The correct answer was HTML")

# ----------------Third question----------------
# Question
print("""
What is 12 * 12?

A. 144
B. 120
C. 1200
D. 1212""")

# Option
third_q = input("Your answer: ")
third_q = third_q.upper()

# Checking
if third_q == "A":
    print("Correct Answer!")
    count += 1
else:
    print("Incorrect Answer! The correct answer was 144.")

# ----------------Fourth question----------------
# Question
print("""
Which planet is known as the Red Planet?

A. Earth
B. Moon
C. Sun
D. Mars""")

# Option
fourth_q = input("Your answer: ")
fourth_q = fourth_q.upper()

# Checking
if fourth_q == "D":
    print("Correct Answer!")
    count += 1
else:
    print("Incorrect Answer! The correct answer was Mars.")

# ----------------Fifth question----------------
# Question
print("""
Who developed Python?

A. Tayyab abbas
B. Elon Musk
C. Imran Khan
D. Guido van Rossum""")

# Option
fifth_q = input("Your answer: ")
fifth_q = fifth_q.upper()

# Checking
if fifth_q == "D":
    print("Correct Answer!")
    count += 1
else:
    print("Incorrect Answer! The correct answer was Guido van Rossum")

# Final 