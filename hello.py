#Created with prompting via ChatGPT
import os

# Get the name from the environment variable.
# Use a default name if no variable is provided.
name = os.getenv("WHO_TO_GREET", "GitHub Actions Student")

# Print the greeting.
print(f"Hello {name}!")

# Explain where the program is running.
print("This program is running inside GitHub Actions.")

