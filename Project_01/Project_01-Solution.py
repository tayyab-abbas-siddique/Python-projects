# Importing the random module to generate a random number
import random

# Introduction
print("================================")
print("NUMBER GUESSING GAME")
print("================================")


# Generating a computer random number between 1 and 100.
computer_number = random.randint(1, 100)
print("I have selected a number between 1 and 100. \nYou have 7 attempts.")

# Asking the user to give his guess
for attempt in range(1, 8):
    user_guess = int(input("Enter your guess: "))

    # Comparing the user guess with the computer number
    if user_guess > computer_number:
        print("Your guess is greater than my number.")
    elif user_guess < computer_number:
        print("Your guess is less than my number.")
    else:
        print(f"Congratulations! You guessed the number in {attempt} attempts.")
        break

# If the user fails to guess the number in 7 attempts, print a message indicating that they failed and reveal the computer's number.
else:
    print(f"You failed to guess the number in 7 attempts. The number was {computer_number}.")