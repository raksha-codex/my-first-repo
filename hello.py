import random

# List of quotes
quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "Experience is the name everyone gives to their mistakes.",
    "First, solve the problem. Then, write the code.",
    "In order to be irreplaceable, one must always be different.",
    "Fix the cause, not the symptom."
]

def show_random_quote():
    quote = random.choice(quotes)
    print("\n💡 Quote of the Day:")
    print(f"\"{quote}\"")

if __name__ == "_main_":
    show_random_quote()