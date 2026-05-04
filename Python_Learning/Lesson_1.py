import os
os.system('cls' if os.name == 'nt' else 'clear')
 
#  1. We still say hello
print("Hello, World!")

# 2. Ask the user a question and save their answer in a variable called 'user_name'
user_name = input("What is your name? ")

# 3. Print a customized message using an "f-string" (the modern Python way!)
print(f"It is great to meet you, {user_name}!")

# 4. Let's do some math! 
# We use int() around the input to tell Python: "Treat this answer as a math Number, not Text"
age = int(input("How old are you? "))
future_age = age + 10

print(f"Wow, in 10 years, you will be {future_age} years old!")

# 5. Making Decisions (If / Else)
# Notice the indentation (the spaces) before the print statements! 
# In Python, indentation tells the computer which code belongs to the 'if' statement.

print("\n--- Bot's Final Thoughts ---")

if age < 18:
    print("You are still young and have so much to explore!")
elif age < 30:
    print("Ah, still in your twenties! A fantastic time of life.")
else:
    print("You have some solid life experience under your belt!")