# Intrduction
print("====== STUDENT INFORMATION ======")

# Asking for each thing
name = input("Enter your name: ") # name
age = int(input("Enter your age: "))  # age
grade = input("Enter your class: ") # grade
school = input("Enter your school: ") # school
fav_sub = input("Enter you favourite subject: ") # favourite subject
enrolled = input("Are you enrolled? ") # Confirmation of enrolled

# My time
print("====== STUDENT PROFILE ======")

# Giving him every thing
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Class: {grade}")
print(f"School: {school}")
print(f"Favourite subject: {fav_sub}")
print(f"Enrolled: {enrolled.capitalize()}")

print("================================")