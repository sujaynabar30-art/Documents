# ==========================================
# Python Mini Calculator
# ==========================================
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("--- Welcome to the Python Mini Calculator ---")

# 1. Get input from the user
# We use float() so the user can enter decimal numbers if they want to.
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

print("\n--- Result ---")

# 2. Make a decision based on the operator they typed
if operator == "+":
    result = num1 + num2
    print(f"The answer is: {num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"The answer is: {num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"The answer is: {num1} * {num2} = {result}")

elif operator == "/":
    # Let's add a safety check! Dividing by zero breaks the universe (and Python).
    if num2 == 0:
        print("Error: You cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"The answer is: {num1} / {num2} = {result}")

else:
    # If they typed a letter or a weird symbol instead of a math operator
    print("Error: Invalid operator! Please run the program again and use +, -, *, or /.")