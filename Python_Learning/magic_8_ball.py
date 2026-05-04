import random
import os

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

print("🔮 Welcome to the Python Magic 8-Ball 🔮")
print("Ask me any yes or no question, and I will predict your future!\n")

# 1. This is a LIST. It holds multiple items inside square brackets [ ].
# Each item is separated by a comma.
fortunes = [
    "Yes, absolutely!",
    "It is certain.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Very doubtful.",
    "Absolutely not."
]

while True:
    # We ask the user for their question, but we don't actually need to save it 
    # for the math, just for the interaction!
    question = input("What is your question? (or type 'quit' to exit): ")

    if question.lower() == 'quit':
        print("The spirits bid you farewell. Goodbye!")
        break
    
    # Check if they just hit enter without typing anything
    if question.strip() == "":
        print("You must ask a question for the spirits to answer!")
        continue

    print("\nThinking...")
    
    # 2. random.choice() looks inside our list and randomly picks exactly one item!
    prediction = random.choice(fortunes)
    
    print(f"🎱 The 8-Ball says: {prediction}\n")
    print("-" * 40) # This just prints a neat little dividing line