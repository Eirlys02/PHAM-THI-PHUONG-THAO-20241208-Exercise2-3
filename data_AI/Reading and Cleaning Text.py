#Reading and Cleaning Text
import string

def load_text_file(filepath):
    lines = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            # Remove whitespace at start/end
            line = line.strip()
            
            # Remove punctuation
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            # Convert to lower case
            line = line.lower()
            
            # Keep non-empty lines
            if line:
                lines.append(line)
    return lines

# Load dataset
text_data = load_text_file("News1.txt")

# Print result
print(len(text_data), "News1.txt")
