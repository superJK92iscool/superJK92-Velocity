import os
import re

# Configure your search directory and replacement
SEARCH_DIR = "./"  # Root folder to scan
TARGET = "NewWord"
REPLACEMENT = "superJK92-Velocity"

# Regex explanation:
#   ("[^"]*?)   -> opening quote and any text before the word, non-greedy
#   \bVelocity\b -> the exact word "Velocity"
#   ([^"]*")    -> any text after it until the closing quote
pattern = re.compile(r'(".*?\b' + re.escape(TARGET) + r'\b.*?")')

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Function that handles replacements inside quoted strings only
    def replacer(match):
        text = match.group(0)
        return text.replace(TARGET, REPLACEMENT)

    new_content = pattern.sub(replacer, content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {file_path}")

def search_and_replace():
    for root, _, files in os.walk(SEARCH_DIR):
        for file in files:
            if file.endswith(".java"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    search_and_replace()
